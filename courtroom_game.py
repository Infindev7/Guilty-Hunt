import pygame
import time

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Courtroom Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Font setup
try:
    font = pygame.font.Font("Fonts/monospace.bold.ttf", 24)
    font_title = pygame.font.Font("Fonts/monospace.medium.ttf", 36)
    font_small = pygame.font.Font("Fonts/monospace.bold.ttf", 18)
except FileNotFoundError:
    print("Custom font not found, using default system font.")
    font = pygame.font.SysFont('Arial', 24)
    font_title = pygame.font.SysFont('Arial', 36)
    font_small = pygame.font.SysFont('Arial', 20)

# Global variables
cases = [
    {
        "title": "The Broken Watch",
        "dialogue": [
            "Narrator: A young woman was found dead in her apartment last night.",
            "Narrator: Cause of death appears to be blunt force trauma. Time of death: around 10:15 PM.",
            "Narrator: No signs of forced entry. Only one suspect was seen near the scene around the time — the Defendant.",
            "Statement by Daniel Royce: I told you, I was just passing by. I don't know what happened!",
            "Statement by Clara Hensley: Witnesses saw him arguing with her. A broken watch at the scene was stopped at 10:15 — the same as the estimated time of death.",
            "Narrator: All statements have been submitted.",
            "You may pass your decision."
        ],
        "is_guilty": True,
        "plaintiff_evidence": [
            {"desc": "Broken watch", "detail": "Found at the scene, stopped at 10:15 PM, matching estimated time of death."},
            {"desc": "Witness report", "detail": "Neighbors reported an argument between the victim and Daniel shortly before the incident."},
            {"desc": "No forced entry", "detail": "Door was intact and locked from inside, suggesting the victim let someone in."},
            {"desc": "CCTV footage", "detail": "Footage near the apartment cuts off at exactly 10:00 PM."}
        ],
        "defendant_evidence": [
            {"desc": "No fingerprints", "detail": "No fingerprints on the murder weapon, a heavy statuette."},
            {"desc": "Alibi witness", "detail": "A man from a nearby food truck claims Daniel bought coffee from him at 10:20 PM."},
            {"desc": "Broken watch", "detail": "Defendant claims the watch's timing is a coincidence and not definitive proof."}
        ],
        "truth": "Daniel struck the victim during a heated argument. The CCTV blackout was orchestrated by him earlier in the day. The food truck vendor misremembered the time."
    },
    {
        "title": "The Stolen Necklace",
        "dialogue": [
            "Narrator: A priceless necklace was stolen from a local jewelry store around 3 PM yesterday.",
            "Narrator: Security footage shows someone entering, and the necklace was discovered missing minutes later.",
            "Narrator: The suspect, Marla Keene, claims innocence and says she only entered to ask for directions.",
            "Statement by Marla Keene: I was just browsing — I never touched anything. I don’t know how the necklace got in my bag.",
            "Statement by Inspector Ray: We found the necklace inside her purse and her fingerprints on the glass case.",
            "Narrator: All statements have been submitted.",
            "You may pass your decision."
        ],
        "is_guilty": True,
        "plaintiff_evidence": [
            {"desc": "Footage", "detail": "Security footage shows Marla entering the store at 3 PM, shortly before the theft."},
            {"desc": "Fingerprints", "detail": "Marla's fingerprints found on the display case where the necklace was kept."},
            {"desc": "Necklace found", "detail": "The stolen necklace was discovered in her bag during a police search."}
        ],
        "defendant_evidence": [
            {"desc": "No tools", "detail": "Marla carried no tools that could be used to open the locked display case."},
            {"desc": "Clean record", "detail": "Marla has no history of theft or criminal behavior."}
        ],
        "truth": "Marla did steal the necklace. She had practiced bypassing the display lock earlier using store visits. Her lack of tools was part of her strategy to appear innocent."
    },
    {
        "title": "The Silent Notes",
        "dialogue": [
            "Narrator: A renowned pianist, Anton Leclair, was found unconscious in his studio. His prized sheet music for an upcoming composition was missing.",
            "Narrator: Only two people were in the building that night — his manager, Eliot Graye, and his student, Clara Duvall.",
            "Statement by Eliot Graye: I came to check in on Anton but didn’t enter the room. Clara had been with him earlier for a long lesson.",
            "Statement by Clara Duvall: I left my lesson at 8 PM sharp. He was fine then. I had no reason to harm him.",
            "Narrator: All statements have been submitted.",
            "You may pass your decision."
        ],
        "is_guilty": False,
        "plaintiff_evidence": [
            {"desc": "Unlocked door", "detail": "Anton’s studio door was unlocked — unusual for him late at night."},
            {"desc": "Missing sheet", "detail": "Only the handwritten composition was taken, while valuables were untouched."},
            {"desc": "Manager’s presence", "detail": "Eliot's office access log shows activity at 8:15 PM — close to the time of the attack."}
        ],
        "defendant_evidence": [
            {"desc": "Lesson time", "detail": "Clara’s lesson ended at 8 PM, verified by building logs."},
            {"desc": "No motive", "detail": "Clara had no known disputes with Anton and was set to perform his work."},
            {"desc": "Manager’s debt", "detail": "Eliot was in severe financial trouble and had motive to sell the composition illicitly."}
        ],
        "truth": "Eliot attacked Anton to steal the composition and sell it under a pseudonym to cover his debts. Clara was uninvolved."
    },
    {
        "title": "The Library Fire",
        "dialogue": [
            "Narrator: A fire broke out in the university archives, destroying rare historical manuscripts.",
            "Narrator: Investigators found signs of arson. Two people were in the vicinity — the archivist Julian Nox and a student researcher, Dana Holt.",
            "Statement by Julian Nox: I locked up early and went home. Dana had been scanning documents all afternoon.",
            "Statement by Dana Holt: I left when the lights flickered. Julian was still inside, or at least his coat was.",
            "Narrator: All statements have been submitted.",
            "You may pass your decision."
        ],
        "is_guilty": True,
        "plaintiff_evidence": [
            {"desc": "Accelerant traces", "detail": "Found near Julian’s desk, not in any other section."},
            {"desc": "Exit badge", "detail": "Julian’s card logged exit at 9:45 PM, same time fire started."},
            {"desc": "Financial motive", "detail": "Julian had applied for a private insurance policy on rare documents the week before."}
        ],
        "defendant_evidence": [
            {"desc": "Dana’s schedule", "detail": "Dana had a recorded library session from 5 to 8 PM."},
            {"desc": "Flickering lights", "detail": "Confirmed by multiple student complaints logged before 9 PM."},
            {"desc": "No direct witness", "detail": "No one saw Julian at the archives post 8 PM."}
        ],
        "truth": "Julian started the fire to claim insurance on privately stored manuscripts. He underestimated how quickly the fire would spread."
    },
    {
        "title": "The Monopolist’s Silence",
        "dialogue": [
            "Narrator: Industrialist Terrance Vale was poisoned during a televised board meeting.",
            "Narrator: Vale had received anonymous threats after hinting at exposing illegal monopoly practices in his own conglomerate.",
            "Narrator: Suspects include his legal aide, Francis Maddox, and his business rival, Elaine Grimmer.",
            "Statement by Francis Maddox: I was in the room, yes, but I poured no drink. I was monitoring the live transcript.",
            "Statement by Elaine Grimmer: I wasn’t even invited. I watched the meeting like everyone else. Vale made enemies, but I wasn’t one of them anymore.",
            "Narrator: All statements have been submitted.",
            "You may pass your decision."
        ],
        "is_guilty": True,
        "plaintiff_evidence": [
            {"desc": "Tainted glass", "detail": "The only glass laced with toxin was the one Vale drank from."},
            {"desc": "Camera blind spot", "detail": "Francis briefly moved out of frame before handing the glass."},
            {"desc": "Login attempt", "detail": "Francis tried accessing Vale's private vault 2 days earlier."},
            {"desc": "Threat email", "detail": "Traced to a burner phone bought with cash near Francis’ apartment."}
        ],
        "defendant_evidence": [
            {"desc": "Live feed proof", "detail": "Camera shows Francis at transcript console during key moments."},
            {"desc": "No poison found", "detail": "No toxin on Francis or his workspace."},
            {"desc": "Grimmer’s motive", "detail": "Elaine had lost a merger deal due to Vale’s veto."}
        ],
        "truth": "Francis poisoned Vale to prevent him from exposing internal documents that would have implicated Francis in insider trading. He exploited the meeting chaos and audio distraction to spike the drink unnoticed."
    },
    {
        "title": "A Bitter Formula",
        "dialogue": [
            "Narrator: Dr. Elena Virelli, a leading pharmaceutical researcher, was found unconscious in her lab.",
            "Narrator: A spilled beaker of corrosive compound was near her, and the lab’s alarm had been manually disabled.",
            "Narrator: Patent files were accessed during the incident. Only Dr. Virelli and her former partner, Dr. Marcus Renner, had lab access.",
            "Statement by Marcus Renner: I was pulling old records during that time. Elena sometimes borrowed my card when rushing.",
            "Statement by Elara Mills: I saw Renner’s ID used at 9:42. Elena didn’t answer my call. The system logs only one entry.",
            "Narrator: All statements have been submitted.",
            "You may pass your decision."
        ],
        "is_guilty": False,
        "plaintiff_evidence": [
            {"desc": "ID log", "detail": "Renner’s card used at 9:42 PM — time of incident."},
            {"desc": "Deleted backup", "detail": "Patent backup deleted at 9:47 PM."},
            {"desc": "Fingerprint", "detail": "Renner’s partial print found on inner door panel."},
            {"desc": "Meeting log", "detail": "Calendar had a meeting set between Renner and Virelli."}
        ],
        "defendant_evidence": [
            {"desc": "CCTV footage", "detail": "Footage shows Renner in another wing at the time of incident."},
            {"desc": "Alarm override", "detail": "Triggered from Elena’s station using her credentials."},
            {"desc": "Keycard report", "detail": "Renner had reported a missing card; both remained active."},
            {"desc": "Chemical analysis", "detail": "Spill pattern consistent with unstable lab condition, not sabotage."}
        ],
        "truth": "Elena disabled the alarm for late-night testing. The accident was due to improper chemical storage. Renner was not present — Elena had used his old keycard, and the deletion of files was automated."
    }
    ,
    {
    "title": "The Minister’s Fund",
    "dialogue": [
        "Narrator: A scandal erupts as ₹50 crores vanish from a government development fund in a remote district.",
        "Narrator: The accused is Minister Rajan Mehta, whose department was responsible for disbursing the funds.",
        "Narrator: An anonymous whistleblower triggered an audit that exposed serious financial discrepancies.",
        "Auditor Ravi Verma: Transaction logs show huge sums transferred to shell companies in a short span.",
        "Auditor Ravi Verma: These companies are all connected to close political associates of Minister Mehta.",
        "Auditor Ravi Verma: We discovered receipts signed by contractors who were declared deceased years ago.",
        "Auditor Ravi Verma: There’s no physical evidence of completed work matching the disbursed amounts.",
        "Minister Rajan Mehta: These claims are politically charged. My office wasn’t informed before the audit.",
        "Minister Rajan Mehta: The firms were selected through official tender processes — I wasn’t directly involved.",
        "Minister Rajan Mehta: I’ve already called for a forensic audit to clear my name from this media circus.",
        "Minister Rajan Mehta: Mismanagement may have occurred, but I deny any personal wrongdoing.",
        "Narrator: All statements have been recorded and the evidence is now in your hands.",
        "You may pass your decision."
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {
            "desc": "Shell links",
            "detail": "Fund transfers went to companies owned by political allies of Minister Mehta."
        },
        {
            "desc": "Dead contractors",
            "detail": "Receipts were signed by contractors who had been deceased for over two years."
        },
        {
            "desc": "Missing developments",
            "detail": "Physical inspections revealed no progress on projects supposedly completed."
        }
    ],
    "defendant_evidence": [
        {
            "desc": "Audit bypass",
            "detail": "Minister Mehta’s office was not formally notified before the audit began, raising legal concerns."
        },
        {
            "desc": "Legal tenders",
            "detail": "Documentation shows that the selected companies fulfilled the tender requirements on paper."
        },
        {
            "desc": "Call for audit",
            "detail": "The minister requested a forensic audit, indicating willingness for transparency."
        }
    ],
    "truth": "Minister Rajan Mehta embezzled development funds by routing money to friendly firms through rigged tenders. The companies were shells created by his political aides. Fabricated paperwork and delayed inquiries were used to cover the trail."
}
,
{
    "title": "The Algorithm Leak",
    "dialogue": [
        "Narrator: TitanCore Technologies recently discovered their proprietary AI trading algorithm was leaked to a foreign competitor.",
        "Narrator: The leak resulted in a loss of ₹300 crores in market valuation within 48 hours.",
        "Narrator: Accused is Aarav Iyer, a senior developer with access to the algorithm’s core modules.",
        "Narrator: Statements from TitanCore's internal security team and Aarav’s defense have been submitted.",
        "Lead Investigator Priya Malhotra: Aarav was one of only five people with unrestricted access to the codebase.",
        "Lead Investigator Priya Malhotra: A USB log shows a large encrypted file copied during his shift two nights before the breach.",
        "Lead Investigator Priya Malhotra: A secured email was sent to an international account linked to a known competitor’s server.",
        "Lead Investigator Priya Malhotra: Aarav’s apartment router shows the IP address tied to that same transfer.",
        "Lead Investigator Priya Malhotra: He had a history of clashing with upper management over compensation and recognition.",
        "Aarav Iyer: I didn’t leak anything. That USB log doesn’t prove what was copied, and I wasn’t even in the office that night.",
        "Aarav Iyer: The CCTV camera on my floor wasn’t working that week. Anyone could’ve used my terminal while I was away.",
        "Aarav Iyer: The IP could have been spoofed. I’ve had phishing attempts and network spoofing incidents reported before.",
        "Aarav Iyer: I submitted a resignation notice weeks ago, why would I sabotage my career?",
        "Aarav Iyer: I also flagged vulnerabilities in our security a month prior — check the internal IT reports.",
        "Narrator: Evidence has been submitted. You're the judge now.",
        "You may pass your decision."
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {
            "desc": "USB file log",
            "detail": "A large encrypted file was copied to an external drive from Aarav’s terminal during an overnight shift."
        },
        {
            "desc": "Unsecured email",
            "detail": "A mail containing encrypted content was sent to a server linked to a rival firm."
        },
        {
            "desc": "Router match",
            "detail": "The sending IP matches Aarav's home router used for remote login the night before the breach."
        },
        {
            "desc": "Motive conflict",
            "detail": "Internal HR reports show repeated clashes between Aarav and senior managers over salary disputes."
        },
        {
            "desc": "Access level",
            "detail": "Aarav was one of five employees with unrestricted access to the full algorithm architecture."
        }
    ],
    "defendant_evidence": [
        {
            "desc": "CCTV failure",
            "detail": "Security footage from the night in question is missing due to a camera outage on Aarav’s office floor."
        },
        {
            "desc": "Spoofed IP risk",
            "detail": "Previous internal reports confirmed Aarav’s router had been targeted in past IP spoofing incidents."
        },
        {
            "desc": "Resignation notice",
            "detail": "Aarav submitted his resignation two weeks prior to the breach, citing burnout, not financial gain."
        },
        {
            "desc": "Security warning report",
            "detail": "Aarav had reported system vulnerabilities a month earlier that went ignored by the IT team."
        },
        {
            "desc": "Terminal access risk",
            "detail": "Aarav’s terminal remained unlocked during lunch hours, and no biometric validation was used."
        }
    ],
    "truth": "Aarav was framed by another team member who wanted to sell the algorithm and cover their tracks. They used his workstation while he was away, took advantage of known router vulnerabilities, and erased CCTV footage from the server. Aarav was a whistleblower, not the thief."
}
,
{
    "title": "The Vault Whisper",
    "dialogue": [
        "Narrator: Three masked individuals executed a high-profile bank heist in Zurich, stealing rare diamonds from a private vault.",
        "Narrator: The robbery plan, including blueprints and security schedules, was leaked two weeks before the heist.",
        "Narrator: Accused is Mikhail Petrov, a Russian security consultant contracted to audit the vault system.",
        "Narrator: The court has received statements from the investigative officer and the accused.",
        "Inspector Delphine Moreau: Mikhail had full access to the internal vault schematics and staff rotation data.",
        "Inspector Delphine Moreau: An anonymous encrypted message with the stolen plan was traced back to his hotel room’s IP.",
        "Inspector Delphine Moreau: His personal device had a decrypted copy of the vault’s layout.",
        "Inspector Delphine Moreau: He checked out of the hotel two days before his contract ended — without informing his client.",
        "Inspector Delphine Moreau: Surveillance shows him meeting with an unidentified individual in a parking garage the same night the message was sent.",
        "Mikhail Petrov: I did have access to the layout — that was my job. The file on my device was part of my audit report.",
        "Mikhail Petrov: The hotel Wi-Fi was unsecured. Anyone could have piggybacked on my IP address.",
        "Mikhail Petrov: I left early due to a family emergency — there are phone logs to prove that.",
        "Mikhail Petrov: The person in the garage was my translator, Layla Chen. She was helping me prepare my exit documentation.",
        "Mikhail Petrov: The company’s internal server had multiple vulnerabilities. Anyone with admin credentials could have leaked the plan.",
        "Narrator: All evidence has been presented. Judge carefully.",
        "You may pass your decision."
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {
            "desc": "Internal access",
            "detail": "Mikhail had clearance to access the most sensitive vault blueprints and schedules."
        },
        {
            "desc": "IP trace",
            "detail": "Encrypted leak message was sent using the hotel room IP where Mikhail was staying."
        },
        {
            "desc": "Decrypted files",
            "detail": "A full vault layout file was found on Mikhail’s laptop."
        },
        {
            "desc": "Early departure",
            "detail": "Mikhail checked out from the hotel two days early without notifying the bank."
        },
        {
            "desc": "Garage footage",
            "detail": "Security camera shows Mikhail meeting a hooded figure hours before the breach message was sent."
        }
    ],
    "defendant_evidence": [
        {
            "desc": "Unsecured Wi-Fi",
            "detail": "Cybersecurity report confirms the hotel’s Wi-Fi was vulnerable to spoofing and packet interception."
        },
        {
            "desc": "Audit protocol",
            "detail": "Bank’s contract required Mikhail to store decrypted layouts for compliance reporting."
        },
        {
            "desc": "Family emergency call",
            "detail": "Mobile provider logs show calls made to a hospital in Moscow the morning before his departure."
        },
        {
            "desc": "Translator alibi",
            "detail": "Layla Chen confirmed meeting Mikhail in the garage to deliver notarized documents."
        },
        {
            "desc": "Server vulnerabilities",
            "detail": "Bank’s internal audit flagged multiple admin accounts with shared passwords."
        }
    ],
    "truth": "The real leak came from a corrupt IT administrator inside the bank, who used Mikhail’s audit credentials to cover their tracks. The parking garage meeting was unrelated, but it was used to paint suspicion. Mikhail was an easy scapegoat due to his foreign nationality and sudden departure."
}
,
{
    "title": "The Masked Beneficiary",
    "dialogue": [
        "Narrator: A multi-million dollar life insurance payout was issued to an individual claiming to be the legal beneficiary of Dr. Koen Tanaka, a renowned robotics researcher presumed dead in a lab fire.",
        "Narrator: The recipient, Samira D’Souza, claims to be Dr. Tanaka’s partner, verified via biometric and video identity verification.",
        "Narrator: A few weeks later, security researchers revealed the identity verification might have been bypassed using AI-generated deepfake video and voice.",
        "Narrator: Samira is now on trial, accused of orchestrating an AI-based fraud to claim the insurance money.",
        "Narrator: Statements from investigators and Samira have been recorded.",
        "Agent Théo Renard: The video submitted to the insurer matches Samira’s face and voice perfectly — but forensic analysis reveals signs of facial warping and synthetic transitions.",
        "Agent Théo Renard: The insurance payout was deposited into a crypto wallet linked to an AI avatar platform previously accessed by Samira’s IP address.",
        "Agent Théo Renard: Dr. Tanaka’s lab had a fail-safe biometric backup key — it was missing from the wreckage, but later found in Samira’s possession.",
        "Agent Théo Renard: Witnesses say Samira disappeared for 72 hours after the fire and gave inconsistent timelines.",
        "Agent Théo Renard: Background checks showed she had searched for AI identity spoofing tools weeks before the incident.",
        "Samira D’Souza: I submitted my ID through the official portal. I had no idea their system could be tricked.",
        "Samira D’Souza: I was Dr. Tanaka’s legal partner. We lived together for three years. I’m listed in his will.",
        "Samira D’Souza: The biometric key was given to me before the accident, for emergencies. I didn’t steal it.",
        "Samira D’Souza: I vanished because I was traumatized. I went to a silent retreat in Bhutan — no internet, no phone.",
        "Samira D’Souza: Those search logs? They’re from our shared device. Koen himself was researching deepfake vulnerabilities!",
        "Narrator: All facts have been presented. The digital trail is real, but so is human error. Choose wisely.",
        "You may pass your decision."
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {
            "desc": "Deepfake artifacts",
            "detail": "Forensic AI tools identified anomalies in the facial structure and frame transitions of Samira’s verification video."
        },
        {
            "desc": "Crypto wallet link",
            "detail": "The insurance funds were deposited to a wallet tied to an AI avatar site previously accessed by Samira."
        },
        {
            "desc": "Biometric key found",
            "detail": "The backup biometric key from Dr. Tanaka’s lab, supposed to be destroyed in the fire, was recovered from Samira’s belongings."
        },
        {
            "desc": "Missing 72 hours",
            "detail": "Samira gave conflicting accounts about her location following the fire and could not produce travel records."
        },
        {
            "desc": "AI tool search logs",
            "detail": "Browser history showed multiple visits to forums discussing bypassing identity checks using synthetic media."
        }
    ],
    "defendant_evidence": [
        {
            "desc": "Legitimate relationship",
            "detail": "Multiple neighbors and work colleagues confirmed that Samira and Dr. Tanaka cohabited for years."
        },
        {
            "desc": "Official verification used",
            "detail": "Samira used the standard insurer portal and submitted verification without any reported glitches."
        },
        {
            "desc": "Will documents",
            "detail": "Signed legal documents list Samira as a primary beneficiary in Dr. Tanaka’s estate."
        },
        {
            "desc": "Mental breakdown",
            "detail": "Psychological evaluation supports Samira’s claim of dissociation and trauma after the fire."
        },
        {
            "desc": "Shared device",
            "detail": "The searches about AI spoofs were made on a shared laptop that Koen also used in his research."
        }
    ],
    "truth": "Samira fabricated a deepfake identity video using AI tools to pass the insurer’s biometric gate. Though she was once Dr. Tanaka’s partner, their relationship had ended weeks before the incident. She kept the biometric key and used knowledge gained from Koen’s own research to execute the fraud. Her alibi was fabricated using travel photos and staged retreat evidence."
}

]


case_index = 0
result_text = ""
case_finished_time = 0
dialogue_index = 0  # Track which dialogue line to display
verdict = None
current_text = ""           # The current dialogue being shown
char_index = 0              # Index of the character being typed
text_timer = 0              # Timer to control type speed
text_speed = 0.03           # Time (seconds) between each character



# Draw case title
def draw_case_title(case):
    title_text = font_title.render(case["title"], True, WHITE)
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 20))


def draw_wrapped_text(text, font, color, x_center, y_start, max_width, line_spacing=10):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)  # Add the last line

    y = y_start
    for line in lines:
        rendered = font.render(line.strip(), True, color)
        x = x_center - rendered.get_width() // 2
        screen.blit(rendered, (x, y))
        y += rendered.get_height() + line_spacing

    return y



# Draw the dialogue (text between plaintiff and defendant)
# Draw the dialogue (text between plaintiff and defendant)
def draw_dialogue(case):
    global char_index, text_timer

    if dialogue_index < len(case["dialogue"]):
        full_line = case["dialogue"][dialogue_index]

        now = time.time()
        if now - text_timer > text_speed and char_index < len(full_line):
            char_index += 1
            text_timer = now

        displayed_text = full_line[:char_index]

        # Use draw_wrapped_text to handle text wrapping
        draw_wrapped_text(
            text=displayed_text,
            font=font,
            color=WHITE,
            x_center=screen.get_width() // 2,
            y_start=100,  # Adjust Y-position if needed
            max_width=800  # Limit width so it wraps instead of going offscreen
        )

        # Show "Press anywhere to continue" only if the line is fully displayed
        if char_index >= len(full_line):
            continue_text = font_small.render("Press anywhere to continue", True, WHITE)
            screen.blit(
                continue_text,
                (screen.get_width() // 2 - continue_text.get_width() // 2, screen.get_height() - 100)
            )  # Position 100px above the bottom of the screen
    else:
        # Keep displaying the last line if all dialogue is finished
        last_line = case["dialogue"][-1]
        draw_wrapped_text(
            text=last_line,
            font=font,
            color=WHITE,
            x_center=screen.get_width() // 2,
            y_start=100,
            max_width=800
        )

# Global variable to store the selected evidence detail
selected_evidence_detail = ""

selected_evidence_image = None

# Global variable to store the scroll offset for evidence
evidence_scroll_offset = 0

# Global flag to enable or disable evidence images
ENABLE_EVIDENCE_IMAGES = False

# Draw the evidence (buttons)
def draw_evidence(case):
    global selected_evidence_detail, evidence_scroll_offset, selected_evidence_image
    base_y = 250 + evidence_scroll_offset  # Start drawing evidence below the instruction text

    # Draw Plaintiff's Evidence
    plaintiff_title = font.render("Accuser's Evidence:", True, WHITE)
    screen.blit(plaintiff_title, (50, base_y - 30))
    for index, evidence in enumerate(case["plaintiff_evidence"]):
        evidence_rect = pygame.Rect(50, base_y + index * 30, 400, 25)  # Create a clickable area
        pygame.draw.rect(screen, (54, 54, 54), evidence_rect)  # Draw a background for the evidence
        evidence_text = font_small.render(f"{evidence['desc']}", True, WHITE)
        screen.blit(evidence_text, (evidence_rect.x + 5, evidence_rect.y + 5))  # Add padding

        # Check if the evidence is clicked
        if pygame.mouse.get_pressed()[0] and evidence_rect.collidepoint(pygame.mouse.get_pos()):
            selected_evidence_detail = evidence["detail"]
            if ENABLE_EVIDENCE_IMAGES:  # Only load the image if the feature is enabled
                try:
                    selected_evidence_image = pygame.image.load(f"Images/{evidence['desc']}.png")  # Load the image dynamically
                except FileNotFoundError:
                    selected_evidence_image = None  # Handle missing image gracefully

    # Calculate the height of the plaintiff's evidence section
    plaintiff_section_height = len(case["plaintiff_evidence"]) * 30

    # Draw Defendant's Evidence
    base_y += plaintiff_section_height + 50  # Add spacing between the two sections
    defendant_title = font.render("Defendant's Evidence:", True, WHITE)
    screen.blit(defendant_title, (50, base_y - 30))
    for index, evidence in enumerate(case["defendant_evidence"]):
        evidence_rect = pygame.Rect(50, base_y + index * 30, 400, 25)  # Create a clickable area
        pygame.draw.rect(screen, (54, 54, 54), evidence_rect)  # Draw a background for the evidence
        evidence_text = font_small.render(f"{evidence['desc']}", True, WHITE)
        screen.blit(evidence_text, (evidence_rect.x + 5, evidence_rect.y + 5))  # Add padding

        # Check if the evidence is clicked
        if pygame.mouse.get_pressed()[0] and evidence_rect.collidepoint(pygame.mouse.get_pos()):
            selected_evidence_detail = evidence["detail"]
            if ENABLE_EVIDENCE_IMAGES:  # Only load the image if the feature is enabled
                try:
                    selected_evidence_image = pygame.image.load(f"Images/{evidence['desc']}.png")  # Load the image dynamically
                except FileNotFoundError:
                    selected_evidence_image = None  # Handle missing image gracefully

    # Calculate the height of the defendant's evidence section
    defendant_section_height = len(case["defendant_evidence"]) * 30

    # Display the selected evidence detail on the right side of the screen
    if selected_evidence_detail:
        detail_title = font.render("Evidence Detail:", True, WHITE)
        screen.blit(detail_title, (600, 200))  # Position the title
        detail_height = draw_wrapped_text(
            text=selected_evidence_detail,
            font=font_small,
            color=WHITE,
            x_center=800,  # Centered on the right side
            y_start=240,
            max_width=300
        )

        # Display the evidence image below the detail
        if ENABLE_EVIDENCE_IMAGES and selected_evidence_image:  # Only display the image if the feature is enabled
            image_x = 800 - 256 // 2  # Center the image with the evidence detail
            image_y = detail_height + 100  # Position 100px below the last line of the evidence detail
            screen.blit(selected_evidence_image, (image_x, image_y))

    # Draw instruction text below the evidence details
    instruction_text = font_small.render("Click the Evidence For Details", True, WHITE)
    screen.blit(instruction_text, (600, 150))  # Position below the evidence details

    # Return the total height of the evidence sections
    return base_y + defendant_section_height


# Draw verdict buttons (Guilty and Innocent)
def draw_verdict_buttons(evidence_bottom_y):
    if verdict is None:  # Only draw buttons if verdict hasn't been given
        innocent_btn = pygame.Rect(50, evidence_bottom_y + 50, 200, 50)  # Position below the evidence
        guilty_btn = pygame.Rect(780, evidence_bottom_y + 50, 200, 50)  # Position below the evidence
        
        # Draw buttons
        pygame.draw.rect(screen, GRAY, innocent_btn)
        pygame.draw.rect(screen, GRAY, guilty_btn)
        
        innocent_text = font.render("Innocent", True, WHITE)
        guilty_text = font.render("Guilty", True, WHITE)
        
        screen.blit(innocent_text, (innocent_btn.x + 40, innocent_btn.y + 10))
        screen.blit(guilty_text, (guilty_btn.x + 55, guilty_btn.y + 10))
        
        return innocent_btn, guilty_btn
    return None, None  # Return None if buttons are not drawn


# Check verdict click
def check_verdict_click(pos, case, evidence_bottom_y):
    global result_text, case_finished_time, verdict  # Add verdict to global variables
    innocent_btn, guilty_btn = draw_verdict_buttons(evidence_bottom_y)  # Pass evidence_bottom_y here
    
    if innocent_btn and innocent_btn.collidepoint(pos):
        verdict = False
    elif guilty_btn and guilty_btn.collidepoint(pos):
        verdict = True
    else:
        return  # No button clicked

    # Determine if the verdict matches the truth
    if verdict == case["is_guilty"]:
        result_text = "Justice"
    else:
        result_text = "Injustice"

    case_finished_time = time.time()


#Case Title Animation
def show_case_intro(case_number, case_title):
    fade_duration = 1.0  # seconds for fade-in and fade-out
    hold_duration = 1.0  # seconds to hold full opacity
    total_duration = fade_duration * 2 + hold_duration
    start_time = time.time()
    
    while True:
        elapsed = time.time() - start_time
        if elapsed > total_duration:
            break

        screen.fill(BLACK)

        # Compute alpha
        if elapsed < fade_duration:
            alpha = int(255 * (elapsed / fade_duration))  # Fade in
        elif elapsed < fade_duration + hold_duration:
            alpha = 255  # Hold full
        else:
            alpha = int(255 * (1 - (elapsed - fade_duration - hold_duration) / fade_duration))  # Fade out

        # Render text surfaces
        title1 = font.render(f"Case No: {case_number}", True, (255, 255, 255))
        title2 = font.render(f"{case_title}", True, (255, 255, 255))

        # Create surfaces with alpha
        title1.set_alpha(alpha)
        title2.set_alpha(alpha)

        # Centered position
        x_center = screen.get_width() // 2
        screen.blit(title1, (x_center - title1.get_width() // 2, 250))
        screen.blit(title2, (x_center - title2.get_width() // 2, 300))

        pygame.display.flip()
        pygame.time.Clock().tick(60)



# Draw the Skip button
def draw_skip_button():
    skip_btn = pygame.Rect(screen.get_width() - 150, 20, 120, 40)  # Position at the top-right corner
    pygame.draw.rect(screen, GRAY, skip_btn)
    skip_text = font.render("Skip", True, WHITE)
    screen.blit(skip_text, (skip_btn.x + 30, skip_btn.y + 5))
    return skip_btn


def show_truth(case):
    while True:
        screen.fill(BLACK)

        # Display the truth
        truth_title = font_title.render("The Truth", True, WHITE)
        truth_text = case["truth"]
        screen.blit(truth_title, (screen.get_width() // 2 - truth_title.get_width() // 2, 100))

        draw_wrapped_text(
            text=truth_text,
            font=font_small,
            color=WHITE,
            x_center=screen.get_width() // 2,
            y_start=200,
            max_width=800
        )

        # Show "Press Anywhere to Continue" at the bottom
        continue_text = font_small.render("Press Anywhere to Continue", True, WHITE)
        screen.blit(continue_text, (screen.get_width() // 2 - continue_text.get_width() // 2, 600))  # Position near the bottom

        pygame.display.flip()

        # Wait for a mouse click to exit the truth screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return  # Exit the function when the player clicks


# Main game loop
def game_loop(): 
    global case_index, result_text, dialogue_index, case_finished_time, verdict, current_text, char_index, text_timer, text_speed, evidence_scroll_offset
    running = True
    show_skip_button = True  # Flag to control the visibility of the Skip button

    # Check if we need to show the intro (fade transition) at the start of the game
    if case_index == 0 and case_finished_time == 0:
        show_case_intro(case_index + 1, cases[case_index]["title"])

    while running:
        screen.fill(BLACK)

        # Get the current case
        case = cases[case_index]

        # Draw case title and dialogue
        draw_case_title(case)
        draw_dialogue(case)

        # Show evidence if dialogue is finished
        if dialogue_index >= len(case["dialogue"]):
            evidence_bottom_y = draw_evidence(case)  # Get the bottom Y position of the evidence sections
            show_skip_button = False  # Hide Skip button when decision frame begins
        
        # Draw verdict buttons only if verdict hasn't been given
        if verdict is None and dialogue_index >= len(case["dialogue"]):
            innocent_btn, guilty_btn = draw_verdict_buttons(evidence_bottom_y)

        # Display the result text if the verdict has been decided
        if result_text:
            color = (0, 255, 0) if result_text == "Justice" else (255, 0, 0)
            result_text_display = font.render(result_text, True, color)
            screen.blit(result_text_display, (screen.get_width() // 2 - result_text_display.get_width() // 2, 600))

        # Draw the Skip button if it should be visible
        if show_skip_button:
            skip_btn = draw_skip_button()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the Skip button is clicked
                if show_skip_button and skip_btn.collidepoint(event.pos):
                    dialogue_index = len(case["dialogue"])  # Skip to the decision frame
                    char_index = 0
                    current_text = ""
                    show_skip_button = False  # Hide Skip button after it's pressed

                # Only move to next dialogue line if current line is fully shown
                elif dialogue_index < len(case["dialogue"]):
                    if char_index >= len(case["dialogue"][dialogue_index]):
                        dialogue_index += 1
                        char_index = 0
                        current_text = ""
                    # Else: ignore click until line is fully rendered

                # When verdict hasn't been decided yet
                elif verdict is None:
                    check_verdict_click(event.pos, case, evidence_bottom_y)  # Pass evidence_bottom_y here
                # Prevent resetting result_text on extra clicks after verdict
                elif result_text and case_finished_time == 0:
                    case_finished_time = time.time()  # Start transition to next case once the verdict is decided

        pygame.display.flip()

        # Transition to next case after a small delay
        if result_text and case_finished_time and time.time() - case_finished_time > 2:  # Wait for 2 seconds before transitioning
            # Show the truth after the verdict
            show_truth(case)

            # Start fade transition before moving to the next case
            if case_index + 1 < len(cases):
                show_case_intro(case_index + 2, cases[case_index + 1]["title"])  # Show intro of next case

            # Move to next case
            case_index += 1
            if case_index >= len(cases):  # If all cases are finished, exit the game
                show_thank_you_message()
                running = False
            else:
                # Reset variables for the next case
                result_text = ""
                dialogue_index = 0
                verdict = None  # Reset verdict for the next case
                case_finished_time = 0  # Reset the case finished time
                show_skip_button = True  # Show Skip button for the next case
                evidence_scroll_offset = 0  # Reset scroll offset for the next case

        pygame.time.Clock().tick(60)




def show_thank_you_message():
    # Display "Thank You For Judging" for 10 seconds
    end_message = font.render("Thank You For Judging", True, WHITE)
    start_time = time.time()
    
    while time.time() - start_time < 5:  # Show message for 10 seconds
        screen.fill(BLACK)
        screen.blit(end_message, (screen.get_width() // 2 - end_message.get_width() // 2, screen.get_height() // 2))
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Keep the game running at 60 FPS



# Start the game
game_loop()

# Quit pygame
pygame.quit()
