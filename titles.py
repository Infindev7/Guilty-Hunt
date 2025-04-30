cases = [
    {
    "title": "The Broken Watch",
    "dialogue": [
        "Narrator: A young woman was found dead in her apartment last night.",
        "Narrator: Cause of death appears to be blunt force trauma. Time of death: around 10:15 PM.",
        "Narrator: No signs of forced entry. Only one suspect was seen near the scene around the time — Daniel Royce.",
        "Statement by Clara Hensley (Accuser): Witnesses saw Daniel arguing with the victim shortly before the incident. A broken watch found at the scene was stopped at 10:15 — exactly the estimated time of death.",
        "Statement by Daniel Royce (Defendant): I was just passing by. I didn’t hurt her! That watch doesn’t prove anything. I even got coffee from a food truck at 10:20 — ask the vendor.",
        "Narrator: All statements have been submitted.",
        "Is Daniel Royce Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Broken watch", "detail": "Found beside the body, stopped at 10:15 PM — time of death."},
        {"desc": "Witness report", "detail": "Multiple neighbors reported hearing an argument between Daniel and the victim shortly before the estimated time of death."},
        {"desc": "No forced entry", "detail": "The apartment was locked from inside, suggesting the victim let her killer in."},
        {"desc": "CCTV cutoff", "detail": "Nearby building footage ends at 10:00 PM. Technicians found manual interruption."}
    ],
    "defendant_evidence": [
        {"desc": "No fingerprints", "detail": "The murder weapon, a heavy statuette, had no usable prints."},
        {"desc": "Alibi claim", "detail": "A food truck vendor claims Daniel purchased coffee at 10:20 PM."},
        {"desc": "Coincidental watch", "detail": "Daniel argues the broken watch could have stopped earlier or later and isn't reliable."}
    ],
    "truth": "Daniel killed the victim in a moment of rage. He had earlier disabled the CCTV system. The food vendor misremembered the time of purchase due to a large crowd at the time."
}

    ,
    {
    "title": "The Stolen Necklace",
    "dialogue": [
        "Narrator: A priceless necklace was stolen from a local jewelry store at approximately 3 PM yesterday.",
        "Narrator: Security footage captured someone entering the premises. Minutes later, the necklace was reported missing.",
        "Narrator: The primary suspect is Marla Keene, who claims she entered only to ask for directions.",
        "Statement by Inspector Ray (Accuser): The necklace was found inside Marla’s bag. Her fingerprints were on the display case. No one else entered the store during that time window.",
        "Statement by Marla Keene (Defendant): I only walked in for directions. I didn’t take anything — maybe someone planted the necklace. And I touched the case because I admired the jewelry, like anyone would.",
        "Narrator: All statements have been submitted.",
        "Is Marla Keene Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Footage", "detail": "Security video shows Marla entering the store alone at 3:00 PM. No other customers were present during the theft window."},
        {"desc": "Fingerprints", "detail": "Her prints were clearly found on the glass covering the stolen necklace."},
        {"desc": "Necklace found", "detail": "The missing necklace was found inside Marla’s handbag during a police search."},
        {"desc": "Unusual behavior", "detail": "The shop clerk recalled Marla moving between display cases repeatedly and staying longer than others asking for directions."}
    ],
    "defendant_evidence": [
        {"desc": "No tools", "detail": "Marla had no equipment capable of breaching the display case, which requires special keys."},
        {"desc": "Clean record", "detail": "Marla has no prior criminal record or suspicious history."},
        {"desc": "No footage of theft", "detail": "The actual moment of the necklace’s disappearance was not caught on camera — only her entry and exit were."}
    ],
    "truth": "Marla planned the theft in advance and had previously observed the case lock mechanism. She used slight-of-hand and familiarity to lift the necklace during a brief distraction. Her plan relied on the absence of tools to make her seem innocent."
}
,
    {
    "title": "The Silent Notes",
    "dialogue": [
        "Narrator: The renowned pianist Anton Leclair was discovered unconscious in his studio. His latest handwritten composition — a highly anticipated debut — was missing.",
        "Narrator: Only two people were known to be in the building that night: Eliot Graye, Anton's long-time manager, and Clara Duvall, his piano student.",
        "Statement by Eliot Graye (Accuser): I only stopped by briefly and never entered Anton's studio. Clara was alone with him earlier, for nearly two hours. I think she left with something more than musical advice.",
        "Statement by Clara Duvall (Defendant): My lesson ended at 8 PM sharp. Anton was well when I left. I wouldn’t steal from someone I admire — I was going to premiere that piece myself.",
        "Narrator: All statements have been submitted.",
        "Is Clara Duvall Guilty?"
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "Unlocked door", "detail": "Anton was known to lock his studio when alone. The door was found ajar — odd unless someone had returned after Clara."},
        {"desc": "Missing sheet", "detail": "The only thing stolen was the handwritten composition, left unsecured on the piano."},
        {"desc": "Access logs", "detail": "Building logs confirm Eliot's office keycard was used at 8:15 PM, moments after Clara left."},
        {"desc": "Eliot's motive", "detail": "Eliot had a gambling problem and was deeply in debt, giving him a reason to profit from selling the stolen work."}
    ],
    "defendant_evidence": [
        {"desc": "Lesson logs", "detail": "Clara's access card shows she exited the building at exactly 8:01 PM."},
        {"desc": "No financial gain", "detail": "Clara had no known financial problems or incentive to profit from the sheet music."},
        {"desc": "Performance plans", "detail": "She was scheduled to publicly debut the composition next week, giving her no reason to sabotage it."},
        {"desc": "Anton’s trust", "detail": "Anton had recently praised Clara as one of the most trustworthy students he'd taught."}
    ],
    "truth": "Eliot entered the studio after Clara left and assaulted Anton to steal the music. He intended to sell it under an alias to cover massive gambling debts. Clara was entirely uninvolved."
}
,
    {
    "title": "The Library Fire",
    "dialogue": [
        "Narrator: A fire broke out in the university archives, devastating priceless historical manuscripts that were irreplaceable.",
        "Narrator: Investigators found signs of arson. Two individuals were in the vicinity at the time: Julian Nox, the archivist, and Dana Holt, a student researcher who was working late.",
        "Statement by Julian Nox (Accuser): I was done for the day and locked up early. Dana was still in the building scanning some rare texts. I left when I was supposed to, and she stayed behind.",
        "Statement by Dana Holt (Defendant): The lights started flickering around 8:50 PM. I was about to leave when I saw Julian's coat still hanging in the office. He wasn’t there when I checked again, but I didn’t think much of it.",
        "Narrator: All statements have been submitted.",
        "Is Julian Nox Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Accelerant traces", "detail": "Traces of an accelerant were found near Julian’s desk, a location only he would have access to."},
        {"desc": "Exit badge log", "detail": "Julian’s access badge logged an exit at 9:45 PM, just when the fire began."},
        {"desc": "Insurance application", "detail": "Julian had taken out a private insurance policy on the rare manuscripts just a week before the fire."},
        {"desc": "Unusual behavior", "detail": "Julian’s behavior was peculiar, being overly cautious in locking up and staying after hours."}
    ],
    "defendant_evidence": [
        {"desc": "Dana’s library session", "detail": "Dana's session logs confirm she was working in the library from 5 PM to 8 PM, but not after."},
        {"desc": "Flickering lights", "detail": "Several students filed complaints about the flickering lights well before 9 PM, verifying Dana’s testimony."},
        {"desc": "No direct sighting", "detail": "There were no witnesses who saw Julian after 8 PM, leaving a gap in the timeline."},
        {"desc": "No motive", "detail": "Dana had no known financial issues and no apparent reason to start a fire in the library."}
    ],
    "truth": "Julian started the fire in an attempt to claim insurance money on rare documents he had privately insured just before the blaze. His overconfidence in the fire’s speed led to the disaster."
}
,
    {
    "title": "The Monopolist’s Silence",
    "dialogue": [
        "Narrator: Terrance Vale, a powerful industrialist, was poisoned during a televised board meeting, collapsing in front of millions.",
        "Narrator: Vale had recently hinted at revealing the illegal monopoly practices inside his own conglomerate, making him enemies within his organization.",
        "Narrator: The main suspects are Francis Maddox, his legal aide, who was present during the meeting, and Elaine Grimmer, a business rival who had much to lose.",
        "Statement by Francis Maddox (Accuser): Yes, I was in the room, but I did not pour the drink. I was busy monitoring the live transcript for the meeting. I never even touched the glass.",
        "Statement by Elaine Grimmer (Defendant): I wasn’t even invited to the meeting. I watched it on live stream, like everyone else. Terrance made a lot of enemies, but I had no stake in his fall. My interests lie elsewhere now.",
        "Narrator: All statements have been submitted.",
        "Is Francis Maddox Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Tainted glass", "detail": "The only glass that Vale drank from was laced with a deadly toxin."},
        {"desc": "Camera blind spot", "detail": "During a crucial moment, Francis moved out of the camera’s frame, possibly giving him a chance to tamper with the drink."},
        {"desc": "Suspicious login attempt", "detail": "Francis tried accessing Vale's private vault 2 days before the incident, something that wasn’t part of his responsibilities."},
        {"desc": "Threat email", "detail": "An anonymous threat email traced to a burner phone purchased near Francis' apartment hinted at an impending reveal about the company’s illegal practices."},
        {"desc": "Financial motive", "detail": "Francis stood to inherit a significant portion of Vale's wealth if he were removed from the picture, especially given Vale’s upcoming exposé."}
    ],
    "defendant_evidence": [
        {"desc": "Live feed proof", "detail": "The security cameras show Francis at the transcript console for several key moments, suggesting he couldn't have poisoned Vale directly."},
        {"desc": "No poison found", "detail": "No traces of poison were found in Francis' personal workspace or on his clothing, clearing him of direct involvement."},
        {"desc": "Motive of Grimmer", "detail": "Elaine Grimmer had just lost a major merger deal to Vale’s veto, giving her a strong motive to eliminate him and regain her financial footing."},
        {"desc": "Meeting chaos", "detail": "The boardroom environment was chaotic during the meeting, with many people distracted, making it easier for someone to poison Vale unnoticed."}
    ],
    "truth": "Francis Maddox poisoned Vale to prevent the exposure of internal documents that would have implicated him in insider trading. The meeting's distractions, combined with the camera blind spot, allowed Francis to spike the drink undetected."
}
,
    {
    "title": "A Bitter Formula",
    "dialogue": [
        "Narrator: Dr. Elena Virelli, a brilliant pharmaceutical researcher, was found unconscious in her lab.",
        "Narrator: A spilled beaker of a corrosive compound was near her, and the lab's alarm system had been manually disabled during the incident.",
        "Narrator: Patent files were accessed around the same time. The only people with access to the lab were Dr. Virelli and her former partner, Dr. Marcus Renner.",
        "Statement by Dr. Marcus Renner (Accuser): I was in another wing of the lab pulling old research records at the time. Elena sometimes borrowed my keycard when she was in a rush.",
        "Statement by Elara Mills (Defendant): I saw Renner's ID used to access the lab at exactly 9:42 PM, which matches the incident time. Elena didn’t answer my call, and the system logs show only one entry, which was Renner’s.",
        "Narrator: All statements have been submitted.",
        "Is Dr. Marcus Renner Guilty?"
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "ID log", "detail": "Renner's ID was used to access the lab at 9:42 PM, around the time of the incident."},
        {"desc": "Deleted backup", "detail": "A patent backup was deleted at 9:47 PM, raising suspicions of tampering."},
        {"desc": "Fingerprint", "detail": "A partial print of Renner was found on the inner door panel, possibly from handling the door."},
        {"desc": "Meeting log", "detail": "A meeting between Dr. Renner and Dr. Virelli was scheduled in the calendar, suggesting possible contact."}
    ],
    "defendant_evidence": [
        {"desc": "CCTV footage", "detail": "Surveillance footage shows Renner in another wing of the lab at the time of the incident, far from the location."},
        {"desc": "Alarm override", "detail": "The lab alarm was manually disabled from Elena’s station using her credentials, not Renner's."},
        {"desc": "Keycard report", "detail": "Renner had reported his keycard as lost earlier, though both his and Elena's cards remained active."},
        {"desc": "Chemical analysis", "detail": "The pattern of the chemical spill suggests a lab accident due to improper storage conditions, not sabotage."}
    ],
    "truth": "Dr. Elena Virelli accidentally caused the chemical spill after disabling the alarm for late-night testing. She used Marcus's old keycard to cover her tracks, and the file deletion was an automated backup. Renner had no involvement in the incident."
}
    ,
    {
    "title": "The Minister’s Fund",
    "dialogue": [
        "Narrator: A scandal erupts as ₹50 crores vanish from a government development fund intended for a remote district.",
        "Narrator: The accused is Minister Rajan Mehta, whose department was responsible for managing and disbursing the funds.",
        "Narrator: An anonymous whistleblower triggered an audit that uncovered major financial discrepancies.",
        "Auditor Ravi Verma (Accuser): Transaction logs show large sums transferred to shell companies in a very short span of time.",
        "Auditor Ravi Verma (Accuser): These companies are linked to close political associates of Minister Mehta, raising questions of conflict of interest.",
        "Auditor Ravi Verma (Accuser): We discovered receipts signed by contractors who had been declared deceased years ago.",
        "Auditor Ravi Verma (Accuser): No physical evidence of completed work exists to match the amounts disbursed to these companies.",
        "Minister Rajan Mehta (Defendant): These claims are politically motivated. My office was not informed of the audit before it began.",
        "Minister Rajan Mehta (Defendant): All firms selected were done so through official tender processes. I was not directly involved in their selection.",
        "Minister Rajan Mehta (Defendant): I've called for a full forensic audit to clear my name from this media circus and the accusations.",
        "Minister Rajan Mehta (Defendant): While there may have been mismanagement, I deny any personal wrongdoing or involvement in embezzlement.",
        "Narrator: All statements have been recorded. The evidence is now in your hands.",
        "You may pass your decision."
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Shell company links", "detail": "Fund transfers went to companies owned by political allies of Minister Mehta."},
        {"desc": "Dead contractors", "detail": "Receipts for work were signed by contractors who had been dead for over two years."},
        {"desc": "Missing developments", "detail": "Physical inspections of the supposed projects revealed no progress or work done at all."}
    ],
    "defendant_evidence": [
        {"desc": "Audit bypass", "detail": "Minister Mehta’s office was not formally notified before the audit began, raising concerns of legal process violations."},
        {"desc": "Legal tender process", "detail": "Documentation shows that the selected companies fulfilled the legal tender requirements on paper, but no further investigation was made."},
        {"desc": "Call for forensic audit", "detail": "The minister's request for a forensic audit indicates a desire for transparency, though it came after the whistleblower’s revelations."}
    ],
    "truth": "Minister Rajan Mehta embezzled development funds by routing money to shell companies owned by his political aides. The companies were set up for the sole purpose of siphoning off public money. The minister used rigged tenders, fabricated documents, and delayed investigations to cover his tracks."
}
,
{
    "title": "The Algorithm Leak",
    "dialogue": [
        "Narrator: TitanCore Technologies recently discovered that their proprietary AI trading algorithm was leaked to a foreign competitor.",
        "Narrator: This leak resulted in a loss of ₹300 crores in market valuation within 48 hours of the breach.",
        "Narrator: The accused is Aarav Iyer, a senior developer with unrestricted access to the core modules of the algorithm.",
        "Narrator: Statements from TitanCore's internal security team and Aarav’s defense have been submitted.",
        "Lead Investigator Priya Malhotra (Accuser): Aarav was one of only five people with unrestricted access to the algorithm’s source code.",
        "Lead Investigator Priya Malhotra (Accuser): A USB log shows that a large encrypted file was copied from Aarav’s terminal during his shift two nights before the breach.",
        "Lead Investigator Priya Malhotra (Accuser): A secured email was sent to an international account linked to a known competitor’s server shortly after the transfer.",
        "Lead Investigator Priya Malhotra (Accuser): Aarav’s apartment router shows the IP address tied to that same transfer.",
        "Lead Investigator Priya Malhotra (Accuser): Aarav had a history of clashing with upper management over compensation and recognition, creating a possible motive.",
        "Aarav Iyer (Defendant): I didn’t leak anything. The USB log doesn’t prove what was copied, and I wasn’t even in the office that night.",
        "Aarav Iyer (Defendant): The CCTV camera on my floor wasn’t working that week. Anyone could have used my terminal while I was away.",
        "Aarav Iyer (Defendant): The IP could have been spoofed. I’ve had phishing attempts and network spoofing incidents reported before.",
        "Aarav Iyer (Defendant): I submitted my resignation weeks ago, why would I sabotage my career by leaking the algorithm?",
        "Aarav Iyer (Defendant): I also flagged vulnerabilities in our security a month prior — check the internal IT reports.",
        "Narrator: Evidence has been submitted. The decision is now yours.",
        "You may pass your decision."
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "USB file log", "detail": "A large encrypted file was copied to an external drive from Aarav’s terminal during his overnight shift."},
        {"desc": "Unsecured email", "detail": "An email containing encrypted content was sent to a server linked to a rival firm."},
        {"desc": "Router match", "detail": "The sending IP address matches Aarav's home router, which was used for remote login the night before the breach."},
        {"desc": "Motive conflict", "detail": "Internal HR reports show repeated clashes between Aarav and senior managers over salary and recognition disputes."},
        {"desc": "Access level", "detail": "Aarav had one of the five highest-level access permissions to the full algorithm architecture."}
    ],
    "defendant_evidence": [
        {"desc": "CCTV failure", "detail": "Security footage from the night in question is missing due to a camera outage on Aarav’s office floor."},
        {"desc": "Spoofed IP risk", "detail": "Internal reports confirmed that Aarav’s router had been targeted in previous IP spoofing incidents."},
        {"desc": "Resignation notice", "detail": "Aarav had submitted his resignation two weeks before the breach, citing burnout and not financial gain as the reason."},
        {"desc": "Security warning report", "detail": "Aarav had reported system vulnerabilities a month earlier, but the IT team ignored his warnings."},
        {"desc": "Terminal access risk", "detail": "Aarav’s terminal remained unlocked during lunch hours, and no biometric validation system was used, increasing the risk of unauthorized access."}
    ],
    "truth": "Aarav was framed by a colleague who wanted to sell the algorithm. The colleague accessed Aarav’s workstation while he was away, took advantage of known router vulnerabilities, and erased CCTV footage from the server. Aarav was a whistleblower, not the thief."
}
,
{
    "title": "The Vault Whisper",
    "dialogue": [
        "Narrator: Three masked individuals executed a high-profile bank heist in Zurich, stealing rare diamonds from a private vault.",
        "Narrator: The robbery plan, including blueprints and security schedules, was leaked two weeks before the heist.",
        "Narrator: Accused is Mikhail Petrov, a Russian security consultant contracted to audit the vault system.",
        "Narrator: The court has received statements from the investigative officer and the accused.",
        "Inspector Delphine Moreau (Accuser): Mikhail had full access to the internal vault schematics and staff rotation data.",
        "Inspector Delphine Moreau (Accuser): An anonymous encrypted message with the stolen plan was traced back to his hotel room’s IP.",
        "Inspector Delphine Moreau (Accuser): His personal device had a decrypted copy of the vault’s layout.",
        "Inspector Delphine Moreau (Accuser): He checked out of the hotel two days before his contract ended — without informing his client.",
        "Inspector Delphine Moreau (Accuser): Surveillance shows him meeting with an unidentified individual in a parking garage the same night the message was sent.",
        "Mikhail Petrov (Defendant): I did have access to the layout — that was my job. The file on my device was part of my audit report.",
        "Mikhail Petrov (Defendant): The hotel Wi-Fi was unsecured. Anyone could have piggybacked on my IP address.",
        "Mikhail Petrov (Defendant): I left early due to a family emergency — there are phone logs to prove that.",
        "Mikhail Petrov (Defendant): The person in the garage was my translator, Layla Chen. She was helping me prepare my exit documentation.",
        "Mikhail Petrov (Defendant): The company’s internal server had multiple vulnerabilities. Anyone with admin credentials could have leaked the plan.",
        "Narrator: All evidence has been presented. The decision is now yours.",
        "You may pass your decision."
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "Internal access", "detail": "Mikhail had clearance to access the most sensitive vault blueprints and schedules."},
        {"desc": "IP trace", "detail": "Encrypted leak message was sent using the hotel room IP where Mikhail was staying."},
        {"desc": "Decrypted files", "detail": "A full vault layout file was found on Mikhail’s laptop."},
        {"desc": "Early departure", "detail": "Mikhail checked out from the hotel two days early without notifying the bank."},
        {"desc": "Garage footage", "detail": "Security camera shows Mikhail meeting a hooded figure hours before the breach message was sent."}
    ],
    "defendant_evidence": [
        {"desc": "Unsecured Wi-Fi", "detail": "Cybersecurity report confirms the hotel’s Wi-Fi was vulnerable to spoofing and packet interception."},
        {"desc": "Audit protocol", "detail": "Bank’s contract required Mikhail to store decrypted layouts for compliance reporting."},
        {"desc": "Family emergency call", "detail": "Mobile provider logs show calls made to a hospital in Moscow the morning before his departure."},
        {"desc": "Translator alibi", "detail": "Layla Chen confirmed meeting Mikhail in the garage to deliver notarized documents."},
        {"desc": "Server vulnerabilities", "detail": "Bank’s internal audit flagged multiple admin accounts with shared passwords."}
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
        "Agent Théo Renard (Accuser): The video submitted to the insurer matches Samira’s face and voice perfectly — but forensic analysis reveals signs of facial warping and synthetic transitions.",
        "Agent Théo Renard (Accuser): The insurance payout was deposited into a crypto wallet linked to an AI avatar platform previously accessed by Samira’s IP address.",
        "Agent Théo Renard (Accuser): Dr. Tanaka’s lab had a fail-safe biometric backup key — it was missing from the wreckage, but later found in Samira’s possession.",
        "Agent Théo Renard (Accuser): Witnesses say Samira disappeared for 72 hours after the fire and gave inconsistent timelines.",
        "Agent Théo Renard (Accuser): Background checks showed she had searched for AI identity spoofing tools weeks before the incident.",
        "Samira D’Souza (Defendant): I submitted my ID through the official portal. I had no idea their system could be tricked.",
        "Samira D’Souza (Defendant): I was Dr. Tanaka’s legal partner. We lived together for three years. I’m listed in his will.",
        "Samira D’Souza (Defendant): The biometric key was given to me before the accident, for emergencies. I didn’t steal it.",
        "Samira D’Souza (Defendant): I vanished because I was traumatized. I went to a silent retreat in Bhutan — no internet, no phone.",
        "Samira D’Souza (Defendant): Those search logs? They’re from our shared device. Koen himself was researching deepfake vulnerabilities!",
        "Narrator: All facts have been presented. The digital trail is real, but so is human error. Choose wisely.",
        "You may pass your decision."
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Deepfake artifacts", "detail": "Forensic AI tools identified anomalies in the facial structure and frame transitions of Samira’s verification video."},
        {"desc": "Crypto wallet link", "detail": "The insurance funds were deposited to a wallet tied to an AI avatar site previously accessed by Samira."},
        {"desc": "Biometric key found", "detail": "The backup biometric key from Dr. Tanaka’s lab, supposed to be destroyed in the fire, was recovered from Samira’s belongings."},
        {"desc": "Missing 72 hours", "detail": "Samira gave conflicting accounts about her location following the fire and could not produce travel records."},
        {"desc": "AI tool search logs", "detail": "Browser history showed multiple visits to forums discussing bypassing identity checks using synthetic media."}
    ],
    "defendant_evidence": [
        {"desc": "Legitimate relationship", "detail": "Multiple neighbors and work colleagues confirmed that Samira and Dr. Tanaka cohabited for years."},
        {"desc": "Official verification used", "detail": "Samira used the standard insurer portal and submitted verification without any reported glitches."},
        {"desc": "Will documents", "detail": "Signed legal documents list Samira as a primary beneficiary in Dr. Tanaka’s estate."},
        {"desc": "Mental breakdown", "detail": "Psychological evaluation supports Samira’s claim of dissociation and trauma after the fire."},
        {"desc": "Shared device", "detail": "The searches about AI spoofs were made on a shared laptop that Koen also used in his research."}
    ],
    "truth": "Samira fabricated a deepfake identity video using AI tools to pass the insurer’s biometric gate. Though she was once Dr. Tanaka’s partner, their relationship had ended weeks before the incident. She kept the biometric key and used knowledge gained from Koen’s own research to execute the fraud. Her alibi was fabricated using travel photos and staged retreat evidence."
}


]

titles = []
for case in cases:
    titles.append(case['title'])

with open('title.txt', 'w') as file:
    for title in titles:
        file.write(f'- {title}\n')