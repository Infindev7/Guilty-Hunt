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

desc_list = {}
for i in cases:
    for key,value in i.items():
        if key == 'plaintiff_evidence' or key == 'defendant_evidence':
            for evidence in value:
                desc_list[evidence['desc']] = evidence['detail']

with open('Desc.txt','w') as file:
    for i,j in desc_list.items():
        file.write(f'- {i}\t:\t{j}\n\n')