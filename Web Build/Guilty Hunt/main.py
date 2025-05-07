import pygame
import time
import sys
import asyncio

# Initialize pygame
pygame.init()

# Load the custom mouse pointer image
try:
    custom_mouse = pygame.image.load("Images/mouse.png")
    custom_mouse = pygame.transform.scale(custom_mouse, (32, 32))  # Resize if needed

    # Set the Pygame window icon
    pygame.display.set_icon(custom_mouse)
except FileNotFoundError:
    print("Custom mouse image not found. Using default mouse pointer.")
    custom_mouse = None

pygame.mouse.set_visible(False)  # Hide the default mouse pointer

# Initialize the mixer for music and SFX
pygame.mixer.init()

# Load the custom mouse pointer image
try:
    custom_mouse = pygame.image.load("Images/mouse.png")
    custom_mouse = pygame.transform.scale(custom_mouse, (32, 32))  # Resize if needed
except FileNotFoundError:
    print("Custom mouse image not found. Using default mouse pointer.")
    custom_mouse = None

# Load music tracks
title_music = "Audio/title_music.mp3"  # Replace with your title screen music file
dialogue_music = "Audio/dialogue_music.mp3"  # Replace with your dialogue/verdict music file
truth_music = "Audio/truth_music.mp3"  # Replace with your truth scene music file
thank_you_music = "Audio/thank_you_music.mp3"  # Replace with your thank-you scene music file

# Load SFX
button_click_sfx = pygame.mixer.Sound("Audio/button_click.wav")  # Replace with your button click SFX file
verdict_sfx = pygame.mixer.Sound("Audio/verdict_sfx.wav")  # Replace with your verdict announcement SFX file

pygame.mixer.music.set_volume(0.5)  # Set volume to 50%

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 760
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Guilty Hunt')

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
    "title": "The Vanishing Vermeer",
    "dialogue": [
        "Narrator: A priceless Vermeer painting, 'The Girl with the Pearl Earring (Replica)', was reported stolen from the private collection of renowned art collector, Alistair Finch.",
        "Narrator: Mr. Finch immediately accused his long-time business partner, Julian Thorne, who had access to the collection and a history of financial difficulties.",
        "Narrator: Julian Thorne vehemently denies the accusations and presents a seemingly solid alibi for the night of the theft.",
        "Narrator: Statements from the accuser and the accused have been recorded.",
        "Alistair Finch (Accuser): Julian was the only one with unsupervised access to my vault besides myself. He knew the security protocols intimately.",
        "Alistair Finch (Accuser): Julian had significant debts and had recently inquired about the insurance value of the Vermeer.",
        "Alistair Finch (Accuser): My security system registered a brief отключение питания (power outage) around the estimated time of the theft, which Julian would have been aware of.",
        "Alistair Finch (Accuser): A witness saw a figure resembling Julian's build leaving my property late that night, though they couldn't identify the face.",
        "Alistair Finch (Accuser): Julian has been evasive and uncooperative with the police investigation.",
        "Julian Thorne (Defendant): I was at an out-of-town conference that entire evening. I have hotel receipts and several colleagues who can vouch for my presence.",
        "Julian Thorne (Defendant): Alistair and I have been friends and business partners for years. I would never betray his trust.",
        "Julian Thorne (Defendant): The hotel I stayed at provides complimentary late-night snacks in the lobby. I have a receipt for a coffee and a pastry at 11:47 PM.",
        "Julian Thorne (Defendant): While I did ask about the insurance value, it was purely out of professional curiosity as Alistair's business partner.",
        "Julian Thorne (Defendant): The witness only saw a 'figure.' That could have been anyone.",
        "Narrator: Alibis can be carefully constructed, but even the most meticulous lies often contain a hairline fracture. Examine the details closely.",
        "Is Julian Thorne Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Vault access", "detail": "Julian Thorne possessed a key and the security code to Alistair Finch's private vault."},
        {"desc": "Financial troubles", "detail": "Bank records indicate Julian Thorne was facing mounting debts and loan repayments."},
        {"desc": "Power outage", "detail": "The security system logged a 5-minute power outage between 10:00 PM and 10:05 PM on the night of the theft."},
        {"desc": "Witness sighting", "detail": "A neighbor reported seeing a person matching Julian Thorne's description leaving the Finch residence around 10:30 PM."},
        {"desc": "Evasive behavior", "detail": "Police reports note Julian Thorne's reluctance to answer specific questions about his whereabouts."}
    ],
    "defendant_evidence": [
        {"desc": "Conference attendance", "detail": "Hotel booking confirmation and conference badge showing Julian Thorne registered and attended the 'Innovate & Invest' conference out of state."},
        {"desc": "Colleague testimonies", "detail": "Three colleagues have provided statements confirming Julian Thorne's presence at the conference dinner and evening networking event."},
        {"desc": "Late-night snack receipt", "detail": "A hotel receipt dated the night of the theft shows a purchase of coffee and a pastry at 11:47 PM from the hotel lobby cafe."},
        {"desc": "Insurance inquiry", "detail": "An email exchange from weeks prior shows Julian Thorne asking about the painting's insured value in the context of updating business asset records."},
        {"desc": "Vague witness", "detail": "The neighbor admitted under questioning that it was dark and they only saw the silhouette of a person."}
    ],
    "truth": "Julian Thorne orchestrated the theft by exploiting his knowledge of the security system. He likely used the power outage as a window to disable key sensors. While he did attend part of the conference, he likely made a brief return trip, relying on the late hour and his familiarity with the property to avoid detection. The flaw in his alibi lies in the *late-night snack receipt*. While it proves he was at the hotel *at 11:47 PM*, it doesn't account for the time *before* that. A quick round trip was possible, and the snack receipt was a planned piece of evidence to solidify his presence later in the evening."
}
    ,
    {
    "title": "The Twisted Testament",
    "dialogue": [
        "Narrator: Elderly millionaire, Beatrice Ainsworth, passed away suddenly. Her will leaves her entire fortune to her newly hired caregiver, Clara Hayes, bypassing her estranged daughter, Eleanor Vance.",
        "Narrator: Eleanor is contesting the will, claiming Clara unduly influenced her frail mother. Clara maintains Beatrice was of sound mind and made her own decisions.",
        "Narrator: Statements from the contesting party and the beneficiary have been recorded.",
        "Eleanor Vance (Accuser): My mother and I had our differences, but she always assured me I would inherit her estate. This sudden change in her will is highly suspicious.",
        "Eleanor Vance (Accuser): Clara was only employed by my mother for three months before her death. It's unlikely a strong bond formed so quickly.",
        "Eleanor Vance (Accuser): My mother was on heavy medication for a heart condition. Clara, with no medical background, was solely responsible for administering it.",
        "Eleanor Vance (Accuser): Several of my mother's long-time friends have stated that Beatrice seemed unusually subdued and dependent in Clara's presence.",
        "Eleanor Vance (Accuser): Clara has a history of working for wealthy elderly individuals, often leaving their employment shortly before or after significant financial events.",
        "Clara Hayes (Defendant): Beatrice and I formed a deep connection in a short time. She appreciated my care and companionship.",
        "Clara Hayes (Defendant): Beatrice explicitly stated her reasons for changing the will in a signed addendum, citing Eleanor's long absence and lack of contact.",
        "Clara Hayes (Defendant): I meticulously followed the dosage instructions provided by Beatrice's doctor for all her medication.",
        "Clara Hayes (Defendant): Beatrice's friends may have been biased due to their long-standing relationship with Eleanor.",
        "Clara Hayes (Defendant): My employment history shows I am a dedicated caregiver who often forms close bonds with my clients.",
        "Narrator: The bonds of family are strong, but so can be the allure of fortune. Look for the inconsistencies that betray the truth.",
        "Is Clara Hayes Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Sudden will change", "detail": "Beatrice Ainsworth's will was amended just weeks before her death, leaving everything to Clara Hayes."},
        {"desc": "Short employment", "detail": "Clara Hayes was employed as Beatrice's caregiver for only three months prior to her passing."},
        {"desc": "Medication management", "detail": "Clara Hayes, without formal medical training, was solely responsible for administering Beatrice's heart medication."},
        {"desc": "Witness accounts", "detail": "Testimonies from Beatrice's friends describe a noticeable change in her demeanor, becoming unusually passive while in Clara's care."},
        {"desc": "Employment history", "detail": "Records show Clara Hayes has worked for three other elderly individuals who experienced significant financial changes shortly before or after her departure."}
    ],
    "defendant_evidence": [
        {"desc": "Signed addendum", "detail": "A signed and notarized addendum to Beatrice's will explicitly states her desire to leave her estate to Clara, citing Eleanor's lack of contact over several years."},
        {"desc": "Doctor's instructions", "detail": "Clara Hayes possesses a written document from Beatrice's physician outlining the medication schedule and dosage."},
        {"desc": "Positive client references", "detail": "Clara provided glowing references from previous clients and their families, praising her care and compassion."},
        {"desc": "Eleanor's absence", "detail": "Evidence, including phone records and correspondence, confirms Eleanor Vance had limited contact with her mother in the years leading up to her death."},
        {"desc": "Independent notary", "detail": "The will addendum was signed in the presence of an independent notary public, who attested to Beatrice's apparent understanding and intent."}
    ],
    "truth": "Clara Hayes subtly manipulated Beatrice through careful control of her medication. While she followed the *dosage instructions*, she likely adjusted the *timing* of the medication to influence Beatrice's mental state when the will addendum was signed. The flaw lies in the *doctor's instructions*. While it details the dosage, it likely *doesn't specify the exact times* the medication should be administered, giving Clara the opportunity to exploit this ambiguity to her advantage. The signed addendum and notary's presence create a veneer of legitimacy, but Beatrice's mental clarity at the time of signing was compromised by Clara's manipulation of her medication schedule."
}
,
    {
    "title": "The Vanishing Violinist",
    "dialogue": [
        "Narrator: Renowned violinist, Maestro Julian Thorne (yes, another Thorne!), disappeared from his locked dressing room during intermission of a sold-out concert. There were no signs of forced entry. His protégé, a talented but ambitious young violinist named Anya Sharma, is the prime suspect.",
        "Narrator: Anya claims she was backstage the entire intermission, preparing for the second act. Both sides present their accounts.",
        "Stage Manager (Accuser): I personally checked Maestro Thorne's dressing room just before the intermission ended, and it was locked from the inside with no response. After forcing the door, the room was empty, and the only window was bolted shut.",
        "Orchestra Member (Accuser): Anya was visibly nervous and agitated before the concert. I overheard her having a heated phone conversation in the hallway.",
        "Security Guard (Accuser): The only person I saw enter or exit the backstage area during the entire intermission was Anya Sharma. No one else.",
        "Maestro Thorne's Agent (Accuser): Maestro Thorne had recently informed Anya that her solo performance in the upcoming international tour would be cut, which caused significant friction between them.",
        "Anya Sharma (Defendant): I was devastated by Maestro Thorne's disappearance. He was my mentor and a great inspiration.",
        "Anya Sharma (Defendant): I remained in my own dressing room during the entire intermission, practicing a difficult passage for the second act. Several orchestra members saw me there.",
        "Anya Sharma (Defendant): I was nervous before the concert because it was a very important performance for me.",
        "Anya Sharma (Defendant): The phone call I had was with my mother, who was feeling unwell. It had nothing to do with Maestro Thorne.",
        "Anya Sharma (Defendant): I have no motive to harm Maestro Thorne. His guidance was crucial for my career.",
        "Orchestra Member 1 (Defendant Witness): I saw Anya in her dressing room during part of the intermission, she was practicing intensely.",
        "Orchestra Member 2 (Defendant Witness): Yes, I also saw Anya in her room, tuning her violin and looking focused.",
        "Narrator: In the silence between the notes, secrets can be hidden. Examine the timeline and the seemingly irrefutable facts.",
        "Is Anya Sharma Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Locked room, no exit", "detail": "Maestro Thorne's dressing room was locked from the inside, with the only window bolted shut."},
        {"desc": "Anya only backstage", "detail": "Security confirms Anya Sharma was the only individual seen entering or exiting the backstage area during the intermission."},
        {"desc": "Heated phone call", "detail": "An orchestra member overheard Anya having an agitated phone conversation before the concert."},
        {"desc": "Solo performance cut", "detail": "Maestro Thorne had recently informed Anya that her solo on the upcoming tour was cancelled."},
        {"desc": "Anya's nervousness", "detail": "Witnesses noted Anya appeared unusually nervous and on edge before the performance."}
    ],
    "defendant_evidence": [
        {"desc": "Devastated by disappearance", "detail": "Anya Sharma expressed shock and sadness regarding Maestro Thorne's disappearance."},
        {"desc": "Practicing in dressing room", "detail": "Anya claims she spent the entire intermission practicing in her own dressing room."},
        {"desc": "Mother's phone call", "detail": "Anya states the agitated phone call was with her sick mother."},
        {"desc": "No motive", "detail": "Anya asserts that Maestro Thorne's mentorship was vital for her career, negating a motive for harm."},
        {"desc": "Witness 1: Saw practicing", "detail": "An orchestra member confirms seeing Anya practicing in her dressing room."},
        {"desc": "Witness 2: Saw tuning", "detail": "Another orchestra member corroborates seeing Anya in her room, tuning her violin."}
    ],
    "truth": "Anya Sharma orchestrated Maestro Thorne's disappearance. The flaw lies in the *timeline and the witnesses who saw her*. Anya likely used her knowledge of the backstage layout and the brief period of darkness during a scene change at the very start of the intermission to quickly and silently move Maestro Thorne (perhaps having incapacitated him beforehand) out of his dressing room via a less obvious route – possibly a connecting passage or a rarely used service door she knew about. She then rushed to her own dressing room to establish her alibi by being seen by other orchestra members during the *later* part of the intermission. The stage manager's check occurred towards the *end* of the intermission, by which time Thorne was already gone, and Anya was in her room. The 'heated phone call' was likely part of her plan or a result of the stress of the situation. The cut solo provided a superficial motive for the investigators to focus on, while her actual method was more subtle and relied on exploiting the brief window of opportunity and the layout of the theater. The witnesses saw her, but not for the *entire* intermission, leaving a crucial gap in the early minutes."
}
,
    {
    "title": "The Missing Manuscript",
    "dialogue": [
        "Narrator: Celebrated author, Alistair Finch (yes, the same one from the painting case, a man with a knack for finding himself in the midst of intrigue!), claims his highly anticipated new manuscript has been stolen from his locked study.",
        "Narrator: He accuses his dedicated but recently disgruntled personal assistant, Evelyn Reed, who had access to his home and study.",
        "Narrator: Evelyn vehemently denies the theft and suggests other possibilities. The facts are presented.",
        "Alistair Finch (Accuser): Evelyn was the only person besides myself with a key to my study. The manuscript was on my desk, and now it's gone. There were no signs of forced entry.",
        "Alistair Finch (Accuser): Evelyn became quite upset after I informed her that I would be hiring a new junior assistant, implying her workload might increase.",
        "Alistair Finch (Accuser): I recall seeing Evelyn lingering near my study door the afternoon before the manuscript disappeared. She seemed agitated.",
        "Alistair Finch (Accuser): My cloud storage account, where I usually back up my work, shows no record of the latest version of the manuscript ever being uploaded.",
        "Alistair Finch (Accuser): Evelyn has been unusually quiet and hasn't offered any helpful suggestions regarding the manuscript's disappearance.",
        "Evelyn Reed (Defendant): I have worked for Mr. Finch for five years and have always been loyal and trustworthy. I would never steal from him.",
        "Evelyn Reed (Defendant): While I was initially disappointed about the new assistant, I understood his reasoning and never expressed any threats or resentment.",
        "Evelyn Reed (Defendant): I often stand near his study door waiting for instructions. My being there doesn't imply anything suspicious.",
        "Evelyn Reed (Defendant): Mr. Finch is not always consistent with his tech habits. He frequently forgets to save or upload his work properly.",
        "Evelyn Reed (Defendant): I have been cooperating fully with the police and have no reason to withhold information.",
        "Narrator: Accusations can be easily made, but proof requires more than suspicion. Look for the cracks in the narrative presented against the accused.",
        "Is Evelyn Reed Guilty?"
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "Study key access", "detail": "Evelyn Reed possessed a key to Alistair Finch's private study."},
        {"desc": "Disappointment over new hire", "detail": "Alistair Finch claims Evelyn Reed was visibly upset upon learning about the new junior assistant."},
        {"desc": "Lingering near study", "detail": "Alistair Finch states he saw Evelyn Reed standing near his study door the day before the manuscript went missing."},
        {"desc": "No cloud backup", "detail": "The latest version of the manuscript was not found in Alistair Finch's cloud storage."},
        {"desc": "Evelyn's silence", "detail": "Alistair Finch interprets Evelyn Reed's quiet demeanor after the incident as suspicious."}
    ],
    "defendant_evidence": [
        {"desc": "Loyal service", "detail": "Evelyn Reed has worked for Alistair Finch for five years with no prior incidents of dishonesty."},
        {"desc": "No threats made", "detail": "Evelyn Reed denies expressing any anger or making any threats regarding the new assistant."},
        {"desc": "Routine behavior", "detail": "Other household staff confirm it was common for Evelyn Reed to wait near the study for instructions."},
        {"desc": "Finch's tech habits", "detail": "Testimony from a former colleague of Alistair Finch suggests he was sometimes disorganized with his digital files and backups."},
        {"desc": "Full cooperation", "detail": "Police reports indicate Evelyn Reed has been cooperative and has provided access to her devices for investigation."}
    ],
    "truth": "Alistair Finch, in his usual state of creative disarray, simply misplaced his manuscript. He has a history of being disorganized, particularly with his digital backups, leading him to believe it was never saved to the cloud. His perception of Evelyn's reaction to the new hire was colored by his own stress over the missing work. The flaw lies in Alistair's claim of 'no cloud backup'. While the *latest version* wasn't there, a closer examination of the cloud storage logs would reveal an *earlier draft* with significant portions of the 'missing' content, indicating Alistair likely saved it at some point and then forgot. His assumption that Evelyn's quietness was suspicious is based on his own anxiety and not any concrete evidence of wrongdoing."
}
,
    {
    "title": "The Stage Sabotage",
    "dialogue": [
        "Narrator: During the opening night of a highly anticipated play, a crucial piece of set design malfunctioned, causing a minor injury to the lead actress, Vivian Holloway.",
        "Narrator: The theater's production manager, Marcus Bell, is accused of intentionally sabotaging the set piece.",
        "Narrator: Marcus claims it was a simple mechanical failure due to rushed construction. Both sides present their arguments.",
        "Vivian Holloway (Accuser): This wasn't an accident. Marcus has been openly resentful of my casting in the lead role. He even made a sarcastic comment about 'accidents happening' during rehearsals.",
        "Vivian Holloway (Accuser): The set piece was inspected and deemed safe just hours before the performance. It's too coincidental that it failed only during my scene.",
        "Vivian Holloway (Accuser): After the incident, Marcus seemed oddly calm and didn't express much concern for my well-being.",
        "Director Eleanor Vance (Accuser): Marcus was responsible for the final checks on all set elements. His negligence, at the very least, put my lead actress at risk.",
        "Director Eleanor Vance (Accuser): There were some minor disagreements about budget and design between Marcus and myself, and Vivian's prominent role was a point of contention.",
        "Marcus Bell (Defendant): I've worked in theater for fifteen years. Safety is always my top priority. This was an unfortunate mechanical failure, likely due to a faulty weld we didn't catch in time.",
        "Marcus Bell (Defendant): Vivian is a talented actress, and I've always been professional in my interactions with her. Her interpretation of my comment is unfair.",
        "Marcus Bell (Defendant): I was likely in shock after the incident. My calm demeanor doesn't equate to guilt.",
        "Marcus Bell (Defendant): Rushed deadlines are common in theater. We did our best to ensure everything was safe, but sometimes things slip through the cracks.",
        "Marcus Bell (Defendant): The director and I have creative differences on every production. It's part of the process and doesn't mean I'd endanger anyone.",
        "Narrator: Accidents happen, but so do acts of malice. Can you discern a deliberate act from a tragic mishap?",
        "Is Marcus Bell Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Resentful comment", "detail": "Vivian Holloway recalls Marcus Bell making a pointed remark about 'accidents happening' a few days before the premiere."},
        {"desc": "Timing of failure", "detail": "The set piece malfunctioned precisely during Vivian Holloway's most crucial scene in the first act."},
        {"desc": "Marcus's demeanor", "detail": "Witnesses noted Marcus Bell appeared unusually unemotional and detached immediately following the incident."},
        {"desc": "Budget disputes", "detail": "Emails between Marcus Bell and the director show ongoing disagreements regarding budget cuts affecting set construction."},
        {"desc": "Sole responsibility", "detail": "Marcus Bell was officially designated as the person responsible for the final safety inspection of all set elements."}
    ],
    "defendant_evidence": [
        {"desc": "Mechanical report", "detail": "A post-incident inspection report suggests a weld on a crucial support beam was faulty, potentially due to a manufacturing defect."},
        {"desc": "Professional history", "detail": "Marcus Bell has a long and largely unblemished professional record in theater production."},
        {"desc": "Common disagreements", "detail": "Several crew members can attest to the frequent and sometimes heated creative disagreements between the director and Marcus."},
        {"desc": "Rushed schedule", "detail": "Production schedules reveal an unusually tight timeframe for set construction leading up to opening night."},
        {"desc": "No prior incidents", "detail": "There have been no previous safety incidents or accusations of negligence against Marcus Bell in his career."}
    ],
    "truth": "Marcus Bell did intentionally weaken the weld on the set piece. The flaw lies in the *mechanical report*. While it correctly identifies a faulty weld, a microscopic analysis (which wasn't initially conducted) would reveal *tool markings* indicating the weld was deliberately tampered with *after* its initial construction. Marcus, under pressure from budget cuts and feeling his creative input was being ignored by the director (who heavily favored the lead actress), lashed out in a way that would cause disruption without serious harm, hoping to undermine the production and assert his importance. His calm demeanor afterward was not shock, but a carefully maintained facade."
}
,
    {
    "title": "The Toxic Spill",
    "dialogue": [
        "Narrator: A significant chemical spill occurred at the Apex Chemical Plant, leading to environmental damage in the nearby river. The company's CEO, Ms. Evelyn Reed (familiar name, isn't it?), is being accused of negligence in safety protocols, leading to the spill.",
        "Narrator: Ms. Reed and Apex Chemical maintain the spill was an unforeseen accident due to a rare equipment malfunction. Both sides present their arguments.",
        "Environmental Agency Lead (Accuser): Our analysis of the river water downstream from the plant shows a high concentration of Compound X, a key ingredient manufactured exclusively at Apex Chemical.",
        "Environmental Agency Lead (Accuser): Plant inspection records from the past year reveal several instances of reported minor equipment malfunctions and near-miss incidents.",
        "Environmental Agency Lead (Accuser): Security footage from the night of the spill shows unusual activity near the storage tanks where Compound X is kept, though the individuals involved are not clearly identifiable.",
        "Environmental Agency Lead (Accuser): Apex Chemical's emergency response plan appears to have been implemented slowly and inefficiently, exacerbating the environmental damage.",
        "Environmental Agency Lead (Accuser): A former employee of Apex Chemical has come forward claiming that safety concerns were often dismissed by management to cut costs.",
        "Evelyn Reed (Defendant): We deeply regret the accidental spill and are fully cooperating with the investigation and remediation efforts.",
        "Evelyn Reed (Defendant): The equipment malfunction that caused the spill was a rare and unpredictable event, exceeding the design limitations of the system.",
        "Evelyn Reed (Defendant): The 'unusual activity' on the security footage was likely routine maintenance checks conducted by our night crew.",
        "Evelyn Reed (Defendant): Our emergency response team acted swiftly according to protocol once the breach was detected.",
        "Evelyn Reed (Defendant): The former employee was dismissed for insubordination and has a clear bias against the company.",
        "Apex Chemical's Lead Engineer (Defendant Witness): Our equipment undergoes regular maintenance and safety checks. The failure was due to a latent defect in a component that was not detectable through standard procedures.",
        "Narrator: Scientific evidence can seem definitive, but even experts can have biases or overlook crucial details. Consider all angles.",
        "Is Evelyn Reed Guilty?"
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "Compound X in river", "detail": "Water samples from the river downstream of Apex Chemical show significant levels of Compound X."},
        {"desc": "Past malfunctions", "detail": "Company records indicate three reported minor equipment malfunctions in the six months leading up to the spill."},
        {"desc": "Unusual night activity", "detail": "Security footage shows unidentified individuals near the storage tanks around the time of the spill."},
        {"desc": "Slow response", "detail": "Timeline analysis suggests a delay of over an hour between the initial spill detection and the full implementation of the emergency response plan."},
        {"desc": "Former employee testimony", "detail": "A former Apex Chemical engineer testified that safety concerns were often ignored due to cost-cutting measures."}
    ],
    "defendant_evidence": [
        {"desc": "Rare malfunction", "detail": "The lead engineer's report attributes the failure to a rare fatigue fracture in a critical valve, undetectable by standard inspections."},
        {"desc": "Routine maintenance log", "detail": "Apex Chemical provided a log detailing routine maintenance checks conducted on the night of the spill, potentially explaining the 'unusual activity'."},
        {"desc": "Protocol adherence", "detail": "Apex Chemical claims its emergency response team followed established protocols once the spill was reported."},
        {"desc": "Dismissal for insubordination", "detail": "HR records confirm the former employee was dismissed for insubordination and had a negative performance review history."},
        {"desc": "Independent audit", "detail": "A recent independent safety audit of the plant found Apex Chemical to be generally compliant with industry safety standards."}
    ],
    "truth": "Apex Chemical and Ms. Reed are not guilty of negligence leading to the spill. The flaw lies in the *Environmental Agency's analysis of Compound X*. While it's true Compound X is manufactured at Apex, a more thorough analysis (initially overlooked due to the obvious connection) would reveal trace amounts of a *new, unrecorded byproduct* in the river samples. This byproduct was formed due to an entirely separate, illegal dumping incident upstream from Apex Chemical, possibly from a smaller, unregistered facility. The 'unusual activity' was indeed routine maintenance. The past minor malfunctions were unrelated to the catastrophic failure. The slow initial response was due to the unexpected nature and scale of the spill, not negligence. The former employee's testimony was indeed biased. The independent audit supports Apex's general adherence to safety. The focus on Compound X, while initially logical, blinded investigators to the possibility of a completely external source of pollution."
}
    ,
    {
    "title": "The Bitter Brew",
    "dialogue": [
        "Narrator: The owner of a popular local brewery, Mr. Alistair Finch (he's back for more drama!), collapsed and died after tasting a new experimental beer. Initial toxicology reports indicate the presence of a rare, fast-acting poison. Suspicion falls on his business partner and head brewer, Ms. Clara Hayes (another familiar face!), who had the most access to the brewing process.",
        "Narrator: Ms. Hayes claims it was a tragic accident during experimentation. Both sides present their arguments.",
        "Detective Rossi (Accuser): Ms. Hayes stood to inherit Mr. Finch's share of the brewery, giving her a clear financial motive.",
        "Detective Rossi (Accuser): Witnesses report a tense argument between Mr. Finch and Ms. Hayes earlier that day regarding the direction of the new beer line.",
        "Detective Rossi (Accuser): Security footage from the brewery shows Ms. Hayes adding an unidentified substance to the experimental batch shortly before Mr. Finch tasted it.",
        "Detective Rossi (Accuser): Ms. Hayes's personal computer contained searches for information on fast-acting and untraceable poisons.",
        "Detective Rossi (Accuser): Ms. Hayes was surprisingly calm and collected after Mr. Finch's death, showing little emotional distress.",
        "Ms. Clara Hayes (Defendant): Alistair and I had a strong professional relationship. I was devastated by his sudden death.",
        "Ms. Clara Hayes (Defendant): Creative disagreements are normal in business. Our argument was brief and resolved quickly.",
        "Ms. Clara Hayes (Defendant): The substance I added to the brew was a natural flavoring agent we were experimenting with. It's part of the brewing process.",
        "Ms. Clara Hayes (Defendant): My research into poisons was for a fictional story I'm writing in my spare time.",
        "Ms. Clara Hayes (Defendant): My calm demeanor was due to shock. Everyone reacts to grief differently.",
        "Brewery Employee (Defendant Witness): I saw Clara adding a small vial of liquid to the experimental batch, but she mentioned it was a new type of hops extract they were trying.",
        "Narrator: Grief can manifest in unexpected ways, and motives can be misleading. Look beyond the obvious explanations.",
        "Is Ms. Clara Hayes Guilty"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Financial motive", "detail": "Clara Hayes was the primary beneficiary of Alistair Finch's share of the brewery in the event of his death."},
        {"desc": "Argument witnessed", "detail": "Two employees overheard a heated discussion between Mr. Finch and Ms. Hayes regarding the new beer recipe."},
        {"desc": "Unidentified substance", "detail": "Security footage shows Ms. Hayes adding a small vial of liquid to the experimental brew before Mr. Finch tasted it."},
        {"desc": "Poison search history", "detail": "Ms. Hayes's computer showed recent searches for 'undetectable poisons' and 'fast-acting toxins'."},
        {"desc": "Calm demeanor", "detail": "Several witnesses noted Ms. Hayes appeared unusually composed after Mr. Finch's sudden death."}
    ],
    "defendant_evidence": [
        {"desc": "Claims of devastation", "detail": "Ms. Hayes stated she was deeply saddened by Mr. Finch's passing."},
        {"desc": "Resolved argument", "detail": "Ms. Hayes claims the argument was minor and quickly resolved."},
        {"desc": "Flavoring agent explanation", "detail": "Ms. Hayes asserts the added substance was a natural flavoring for the beer."},
        {"desc": "Fiction writing alibi", "detail": "Ms. Hayes claims her poison research was for a novel she is writing."},
        {"desc": "Shock response", "detail": "Ms. Hayes suggests her calm demeanor was a result of shock."},
        {"desc": "Employee testimony (hops)", "detail": "A brewery employee corroborates seeing Ms. Hayes add a liquid, which she described as a 'hops extract'."}
    ],
    "truth": "Clara Hayes did poison Alistair Finch. The flaw lies in her explanation of the *substance she added* and the *employee's testimony*. While the employee saw her add a liquid and heard her call it 'hops extract,' a closer look at the security footage, specifically the moment of transfer, would reveal Ms. Hayes subtly *swapping* the labeled vial of hops extract with an identical-looking vial containing the poison. She likely prepared this switch beforehand, knowing Mr. Finch would be the first to taste the experimental batch. The employee's testimony is truthful to what they *heard*, but doesn't account for the surreptitious switch. Ms. Hayes used her knowledge of the brewing process and the trust of her colleagues to execute the poisoning. Her 'fiction writing' and 'shock' explanations are convenient lies to deflect suspicion."
}
,
{
    "title": "The Contested Crash",
    "dialogue": [
        "Narrator: A two-car collision occurred at a seemingly straightforward intersection. Driver A, Mr. Harrison, claims Driver B, Ms. Davies, ran a red light, causing the accident.",
        "Narrator: Ms. Davies insists her light was green and that Mr. Harrison was speeding. The police report offers some initial findings, but key ambiguities remain.",
        "Narrator: Both drivers present their accounts of the incident.",
        "Mr. Harrison (Accuser): I had a clear green light. I entered the intersection, and Ms. Davies's car suddenly collided with mine. She must have run the red.",
        "Mr. Harrison (Accuser): My passenger corroborates my statement. He clearly saw the light was green for us.",
        "Mr. Harrison (Accuser): The damage to Ms. Davies's front bumper suggests a high-speed impact, further supporting my claim that she was speeding through a red light.",
        "Mr. Harrison (Accuser): Ms. Davies appeared flustered and disoriented after the accident, which could indicate guilt or awareness of her mistake.",
        "Mr. Harrison (Accuser): My car's dashcam footage clearly shows the traffic light was green as I entered the intersection.",
        "Ms. Davies (Defendant): My light was definitely green. Mr. Harrison must have been distracted or misremembering. He was driving very fast.",
        "Ms. Davies (Defendant): The fact that Mr. Harrison's car sustained more damage indicates he was the one driving recklessly and caused the more forceful impact.",
        "Ms. Davies (Defendant): I braked as soon as I saw his car entering the intersection, which is why the damage to my front is concentrated.",
        "Ms. Davies (Defendant): I was shaken up after the accident, anyone would be. It doesn't mean I was at fault.",
        "Ms. Davies (Defendant): The police report mentions a possible malfunction with the traffic light sequence at that intersection earlier in the week.",
        "Narrator: Eye-witness accounts can be unreliable, and even recordings can be misinterpreted. The truth may lie in the subtle details of the physical evidence.",
        "Is Ms. Davies Guilty?"
    ],
    "is_guilty": False,
    "plaintiff_evidence": [
        {"desc": "Dashcam footage (Harrison)", "detail": "Mr. Harrison's dashcam shows his vehicle entering the intersection while the traffic light directly ahead appears green."},
        {"desc": "Passenger testimony", "detail": "Mr. Harrison's passenger confirms that the light was green for their vehicle."},
        {"desc": "Damage to Davies's bumper", "detail": "The police report notes significant damage to the front of Ms. Davies's vehicle."},
        {"desc": "Harrison's statement", "detail": "Mr. Harrison consistently states that his light was green and Ms. Davies ran a red light."},
        {"desc": "Davies's demeanor", "detail": "Witnesses at the scene noted Ms. Davies appeared agitated and confused after the collision."}
    ],
    "defendant_evidence": [
        {"desc": "More damage to Harrison's car", "detail": "Mr. Harrison's vehicle sustained more extensive damage overall compared to Ms. Davies's car."},
        {"desc": "Davies's braking", "detail": "Skid marks at the scene suggest Ms. Davies applied her brakes before the impact."},
        {"desc": "Davies's statement", "detail": "Ms. Davies consistently maintains that her light was green and Mr. Harrison was speeding."},
        {"desc": "Light malfunction report", "detail": "Police records indicate a report of intermittent traffic light sequence issues at that intersection three days prior to the accident."},
        {"desc": "Concentrated front damage", "detail": "The damage to Ms. Davies's car is primarily concentrated on the front, suggesting she was braking and the impact was head-on."}
    ],
    "truth": "Ms. Davies was indeed telling the truth. The flaw lies in the *interpretation of Mr. Harrison's dashcam footage*. While it shows a green light as his car enters the intersection, a careful frame-by-frame analysis (which wasn't initially done) would reveal a *flicker* or a very brief yellow light just before turning green. Mr. Harrison, eager to proceed, might have accelerated as soon as he saw green without noticing the preceding yellow, especially if he was slightly speeding. His passenger's confirmation is likely based on the same initial perception. The greater damage to Mr. Harrison's car supports the idea that he was traveling at a higher speed. Ms. Davies's braking and the concentrated front-end damage on her car are consistent with her attempt to stop. The reported light malfunction, though days prior, adds a layer of doubt to the reliability of the light sequence at that intersection."
}
,
{
    "title": "The Anonymous Tipster",
    "dialogue": [
        "Narrator: A high-stakes poker game was raided by the police based on an anonymous tip-off alleging illegal gambling and drug use. One of the players, Mr. Sterling, a seemingly reputable businessman, is now being charged with organizing the illegal game.",
        "Narrator: Mr. Sterling denies any involvement in organizing the game and claims he was merely a participant. Both sides present their information.",
        "Detective Miller (Accuser): The anonymous tip was highly specific, detailing the location, time, and individuals involved, including Mr. Sterling as the host.",
        "Detective Miller (Accuser): Upon entering the premises, officers found gambling paraphernalia, large sums of cash, and traces of illegal substances.",
        "Detective Miller (Accuser): Several other attendees identified Mr. Sterling as the one who invited them to the game and provided the location details.",
        "Detective Miller (Accuser): Financial records obtained from the location show a pattern of regular large cash deposits that do not align with the building's legitimate business operations.",
        "Detective Miller (Accuser): Mr. Sterling has a prior, albeit minor, conviction for a related gambling offense from several years ago.",
        "Mr. Sterling (Defendant): I occasionally enjoy a friendly game of poker. I was simply invited to this gathering by someone else whose name I don't recall.",
        "Mr. Sterling (Defendant): The presence of illegal activities doesn't automatically make everyone present guilty of organizing them.",
        "Mr. Sterling (Defendant): I brought my own winnings from previous legitimate games. The cash I had was not related to this event.",
        "Mr. Sterling (Defendant): I have many acquaintances, and it's possible some of them might mistakenly believe I informed them about the game.",
        "Mr. Sterling (Defendant): My past conviction was a youthful indiscretion and has no bearing on this situation.",
        "Mr. Sterling's Lawyer (Defendant Witness): My client is a respected member of the community with a successful business. It is unlikely he would risk his reputation by organizing an illegal gambling operation.",
        "Narrator: Sometimes, the most convincing denials hide the deepest secrets. Look for the inconsistencies in the defendant's story.",
        "Is Mr. Sterling Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Specific anonymous tip", "detail": "The anonymous tip accurately described the location, time, attendees, and identified Mr. Sterling as the organizer."},
        {"desc": "Gambling paraphernalia found", "detail": "Police discovered poker tables, chips, and other gambling-related items at the location."},
        {"desc": "Attendee testimonies", "detail": "Three attendees stated that Mr. Sterling personally invited them to the game via text message."},
        {"desc": "Suspicious cash deposits", "detail": "Financial records for the raided location show regular, large cash deposits with no clear business justification."},
        {"desc": "Prior gambling conviction", "detail": "Mr. Sterling has a record of a misdemeanor conviction for illegal gambling from eight years prior."}
    ],
    "defendant_evidence": [
        {"desc": "Claims of being a guest", "detail": "Mr. Sterling maintains he was merely a participant and did not organize the game."},
        {"desc": "Cash from 'legitimate winnings'", "detail": "Mr. Sterling claims the cash he possessed was from previous, legal poker games."},
        {"desc": "Unrecalled invitation source", "detail": "Mr. Sterling states he was invited by someone he cannot remember."},
        {"desc": "Mistaken identity possibility", "detail": "Mr. Sterling suggests that acquaintances might have mistakenly believed he informed them about the game."},
        {"desc": "Youthful indiscretion", "detail": "Mr. Sterling's lawyer downplays his prior conviction as a minor offense from his youth."},
        {"desc": "Reputable businessman", "detail": "Testimony from Mr. Sterling's lawyer emphasizes his client's standing in the community."}
    ],
    "truth": "Mr. Sterling was indeed the organizer of the illegal poker game. The flaw lies in his claim about the *source of his invitation*. While he pretends not to remember who invited him, a closer examination of his *phone records* (obtained during the investigation but presented as part of the defendant's broader evidence of his 'innocence') would reveal numerous recent text message exchanges with several of the other attendees, coordinating the game's details, location, and buy-in amounts. His attempt to appear as just another guest is contradicted by this digital footprint. His explanation of the cash being from 'legitimate winnings' is a weak attempt to explain the large sum he had on hand, which matched the typical buy-in for the high-stakes game."
}
,
{
    "title": "The Shadowy Figure",
    "dialogue": [
        "Narrator: A valuable piece of technology was stolen from a secure research lab at Quantum Innovations. Security footage shows a shadowy figure entering and leaving the lab late at night. Suspicion falls on Dr. Aris Thorne (another familiar name!), a brilliant but eccentric scientist who had recently been denied access to the specific project related to the stolen technology.",
        "Narrator: Dr. Thorne claims he was at home all night working on his own independent research. Both sides present their arguments.",
        "Lead Investigator Davies (Accuser): Dr. Thorne had motive. He was vocal about his disagreement with being excluded from the 'Project Chimera' and felt his expertise was being overlooked.",
        "Lead Investigator Davies (Accuser): The shadowy figure in the security footage appears to match Dr. Thorne's height and build.",
        "Lead Investigator Davies (Accuser): Dr. Thorne's access badge was used to enter the outer perimeter of the lab facility around the time of the theft, though not the specific lab itself.",
        "Lead Investigator Davies (Accuser): Dr. Thorne's computer logs show unusual file access related to the 'Project Chimera' schematics in the days leading up to the theft.",
        "Lead Investigator Davies (Accuser): When questioned, Dr. Thorne was evasive about his activities that night and couldn't provide concrete proof of being home.",
        "Dr. Aris Thorne (Defendant): I was indeed disappointed about being excluded from 'Project Chimera,' but I would never resort to theft.",
        "Dr. Aris Thorne (Defendant): The security footage is grainy and the figure is obscured. It could be anyone of similar stature.",
        "Dr. Aris Thorne (Defendant): I often work late and might have used my badge to access other areas of the facility for my own research.",
        "Dr. Aris Thorne (Defendant): My file access logs show I was reviewing publicly available information related to similar technologies, not the proprietary 'Project Chimera' schematics.",
        "Dr. Aris Thorne (Defendant): As a scientist, my work hours are often irregular. I was working on complex calculations at home and didn't feel the need to document every minute.",
        "Dr. Thorne's Neighbor (Defendant Witness): I saw Dr. Thorne's light on in his study late that night, around the time of the reported theft. I often see him working late.",
        "Narrator: Circumstantial evidence can paint a picture, but is that picture accurate? Look for alternative interpretations.",
        "Is Dr. Aris Thorne Guilty?"
    ],
    "is_guilty": True,
    "plaintiff_evidence": [
        {"desc": "Motive: Project exclusion", "detail": "Dr. Thorne had expressed frustration about being excluded from the 'Project Chimera' team."},
        {"desc": "Similar build", "detail": "The shadowy figure in the security footage has a similar height and build to Dr. Thorne."},
        {"desc": "Perimeter badge access", "detail": "Dr. Thorne's access badge was used to enter the outer security perimeter of the lab facility at 11:17 PM."},
        {"desc": "Unusual file access", "detail": "Computer logs show Dr. Thorne accessed several files containing keywords related to 'Project Chimera' in the days before the theft."},
        {"desc": "Evasive questioning", "detail": "Investigator notes indicate Dr. Thorne was hesitant and vague when asked about his whereabouts on the night of the theft."}
    ],
    "defendant_evidence": [
        {"desc": "Grainy footage", "detail": "The security footage of the intruder is low-resolution and the figure's features are obscured."},
        {"desc": "Legitimate badge use", "detail": "Dr. Thorne often works late and has legitimate reasons to access the outer facility for his independent research."},
        {"desc": "Public information review", "detail": "Dr. Thorne claims his file access was related to publicly available research on similar technologies."},
        {"desc": "Irregular work hours", "detail": "Dr. Thorne's neighbor confirms he often works late into the night at home."},
        {"desc": "No forced entry", "detail": "There were no signs of forced entry into the specific lab where the technology was stolen, suggesting someone with authorized access was involved."}
    ],
    "truth": "Dr. Thorne did steal the technology. The flaw lies in his explanation of his *computer file access*. While he claims he was reviewing publicly available information, a forensic analysis of his recently deleted browsing history (which he thought he had permanently erased) would reveal specific searches for *internal project documentation* and detailed specifications of the stolen technology, far beyond what would be publicly available. He accessed these files using his legitimate credentials before his access was revoked. His perimeter badge access provided him the opportunity to enter the facility, and he likely used his knowledge of the security systems and the fact that his access to the specific lab had only recently been revoked to his advantage. The shadowy figure's similar build and his evasiveness further support his guilt."
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
text_speed = 0.0001           # Time (seconds) between each character
moral_meter = 0.0  # Tracks the player's moral score


def play_music(track, loop=True):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1 if loop else 0)  # Loop indefinitely if `loop` is True

def stop_music():
    pygame.mixer.music.stop()


def calculate_moral_count(case):
    total_characters = sum(len(line) for line in case["dialogue"])
    return round(total_characters / 1000, 2)


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
ENABLE_EVIDENCE_IMAGES = True

# Global variables for the progress bar
verdict_timer_start = None  # Tracks when the timer starts
VERDICT_TIME_LIMIT = 120  # Time limit in seconds (2 minutes)

# Draw the evidence (buttons)
def draw_evidence(case):
    global selected_evidence_detail, evidence_scroll_offset, selected_evidence_image
    base_y = 250 + evidence_scroll_offset  # Start drawing evidence below the instruction text

    # Draw Plaintiff's Evidence
    plaintiff_title = font.render("Accuser's Evidence:", True, WHITE)
    screen.blit(plaintiff_title, (25, base_y - 30))
    for index, evidence in enumerate(case["plaintiff_evidence"]):
        evidence_rect = pygame.Rect(25, base_y + index * 30, 400, 25)  # Create a clickable area
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
    screen.blit(defendant_title, (25, base_y - 30))
    for index, evidence in enumerate(case["defendant_evidence"]):
        evidence_rect = pygame.Rect(25, base_y + index * 30, 400, 25)  # Create a clickable area
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
        screen.blit(detail_title, (500, 200))  # Position the title
        detail_height = draw_wrapped_text(
            text=selected_evidence_detail,
            font=font_small,
            color=WHITE,
            x_center=700,  # Centered on the right side
            y_start=240,
            max_width=300
        )

        # Display the evidence image below the detail
        if ENABLE_EVIDENCE_IMAGES and selected_evidence_image:  # Only display the image if the feature is enabled
            image_x = 700 - 256 // 2  # Center the image with the evidence detail
            image_y = detail_height + 25  # Position 100px below the last line of the evidence detail
            screen.blit(selected_evidence_image, (image_x, image_y))

    # Draw instruction text below the evidence details
    instruction_text = font_small.render("Click the Evidence For Details", True, WHITE)
    screen.blit(instruction_text, (600, 150))  # Position below the evidence details

    # Return the total height of the evidence sections
    return base_y + defendant_section_height


# Draw verdict buttons (Guilty and Innocent)
def draw_verdict_buttons(evidence_bottom_y):
    if verdict is None:  # Only draw buttons if verdict hasn't been given
        innocent_btn = pygame.Rect(25, evidence_bottom_y + 50, 200, 50)  # Position below the evidence
        guilty_btn = pygame.Rect(750, evidence_bottom_y + 50, 200, 50)  # Position below the evidence
        
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
    global result_text, case_finished_time, verdict, verdict_timer_start, moral_meter
    innocent_btn, guilty_btn = draw_verdict_buttons(evidence_bottom_y)

    # Check if the time has run out
    if verdict_timer_start is not None and time.time() - verdict_timer_start > VERDICT_TIME_LIMIT:
        verdict = "timeout"
        result_text = "Time Out"
        moral_count = calculate_moral_count(case)
        moral_meter -= moral_count / 2  # Subtract half of the moral count for a timeout
        pygame.mixer.Sound.play(verdict_sfx)  # Play verdict SFX
        case_finished_time = time.time()
        return

    if innocent_btn and innocent_btn.collidepoint(pos):
        verdict = False
    elif guilty_btn and guilty_btn.collidepoint(pos):
        verdict = True
    else:
        return  # No button clicked

    # Determine if the verdict matches the truth
    moral_count = calculate_moral_count(case)
    if verdict == case["is_guilty"]:
        result_text = "Justice"
        moral_meter += moral_count  # Add moral count for justice
    else:
        result_text = "Injustice"
        moral_meter -= moral_count  # Subtract moral count for injustice

    pygame.mixer.Sound.play(verdict_sfx)  # Play verdict SFX
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

        # Draw the custom mouse pointer
        if custom_mouse:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(custom_mouse, (mouse_x, mouse_y))

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
    play_music(truth_music, loop=True)  # Play truth music once
    while True:
        screen.fill(BLACK)

        # Display the truth
        truth_title = font_title.render("The Truth", True, WHITE)
        truth_text = case["truth"]
        screen.blit(truth_title, (screen.get_width() // 2 - truth_title.get_width() // 2, 25))

        draw_wrapped_text(
            text=truth_text,
            font=font_small,
            color=WHITE,
            x_center=screen.get_width() // 2,
            y_start=100,
            max_width=850
        )

        # Show "Press Anywhere to Continue" at the bottom
        continue_text = font_small.render("Press Anywhere to Continue", True, WHITE)
        screen.blit(continue_text, (screen.get_width() // 2 - continue_text.get_width() // 2, 600))  # Position near the bottom

        # Draw the custom mouse pointer
        if custom_mouse:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(custom_mouse, (mouse_x, mouse_y))

        pygame.display.flip()

        # Wait for a mouse click to exit the truth screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                stop_music()  # Stop truth music
                return  # Exit the function when the player clicks
            

def draw_moral_meter():
    # Draw the moral meter label
    moral_label = font_small.render("Moral Meter", True, WHITE)
    screen.blit(moral_label, (screen.get_width() // 2 - moral_label.get_width() // 2, screen.get_height() - 110))

    # Draw the current moral meter value
    moral_value = font.render(f"{moral_meter:.2f}", True, WHITE)
    screen.blit(moral_value, (screen.get_width() // 2 - moral_value.get_width() // 2, screen.get_height() - 90))


def draw_progress_bar():
    if verdict_timer_start is not None:
        # Calculate elapsed time
        elapsed_time = time.time() - verdict_timer_start
        remaining_time = max(0, VERDICT_TIME_LIMIT - elapsed_time)

        # Draw the progress bar background (vertical)
        bar_width = 20
        bar_height = 600
        bar_x = 975  # 50px away from the left edge
        bar_y = (screen.get_height() - bar_height) // 2
        pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height))

        # Draw the progress bar fill (vertical)
        progress_height = int((remaining_time / VERDICT_TIME_LIMIT) * bar_height)
        pygame.draw.rect(screen, WHITE, (bar_x, bar_y + (bar_height - progress_height), bar_width, progress_height))

        # Draw the "Time" label at the top of the bar
        time_label = font_small.render("Time", True, WHITE)
        screen.blit(time_label, (bar_x + bar_width // 2 - time_label.get_width() // 2, bar_y - 30))

        # Draw the remaining time at the bottom of the bar
        time_text = font_small.render(f"{int(remaining_time)}s", True, WHITE)
        screen.blit(time_text, (bar_x + bar_width // 2 - time_text.get_width() // 2, bar_y + bar_height + 10))


def show_title_screen():
    # Play title screen music
    play_music(title_music, loop=True)
    pygame.mixer.music.set_volume(0.5)  # Ensure volume is set

    # Load the title image
    try:
        title_image = pygame.image.load("Images/title_image.png")  # Replace with your title image path
        title_image = pygame.transform.scale(title_image, (700, 400))  # Resize the image if needed
    except FileNotFoundError:
        print("Title image not found. Using placeholder text.")
        title_image = None

    # Slider values
    music_volume = 0.5
    sfx_volume = 0.5

    # Slider positions
    music_slider_rect = pygame.Rect(650, 535, 200, 20)
    sfx_slider_rect = pygame.Rect(650, 645, 200, 20)

    # Button positions
    start_button = pygame.Rect(200, 520, 200, 50)
    quit_button = pygame.Rect(200, 620, 200, 50)

    running = True
    while running:
        screen.fill(BLACK)

        # Draw the title image or placeholder text
        if title_image:
            screen.blit(title_image, (screen.get_width() // 2 - title_image.get_width() // 2, 25))
        else:
            title_text = font_title.render("Guilty Hunt", True, WHITE)
            screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Draw buttons
        pygame.draw.rect(screen, GRAY, start_button)
        pygame.draw.rect(screen, GRAY, quit_button)
        start_text = font.render("Start", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)
        screen.blit(start_text, (start_button.x + 60, start_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

        # Draw sliders
        pygame.draw.rect(screen, GRAY, music_slider_rect)
        pygame.draw.rect(screen, GRAY, sfx_slider_rect)
        pygame.draw.rect(screen, WHITE, (music_slider_rect.x, music_slider_rect.y, int(music_volume * music_slider_rect.width), music_slider_rect.height))
        pygame.draw.rect(screen, WHITE, (sfx_slider_rect.x, sfx_slider_rect.y, int(sfx_volume * sfx_slider_rect.width), sfx_slider_rect.height))

        # Draw slider labels
        music_label = font_small.render("Music Volume", True, WHITE)
        sfx_label = font_small.render("SFX Volume", True, WHITE)
        screen.blit(music_label, (music_slider_rect.x - 150, music_slider_rect.y))
        screen.blit(sfx_label, (sfx_slider_rect.x - 150, sfx_slider_rect.y))

        # Draw the custom mouse pointer
        if custom_mouse:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(custom_mouse, (mouse_x, mouse_y))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(button_click_sfx)  # Play button click SFX
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(button_click_sfx)  # Play button click SFX
                if start_button.collidepoint(event.pos):
                    stop_music()  # Stop title music
                    return  # Start the game
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif music_slider_rect.collidepoint(event.pos):
                    music_volume = (event.pos[0] - music_slider_rect.x) / music_slider_rect.width
                    pygame.mixer.music.set_volume(music_volume)
                elif sfx_slider_rect.collidepoint(event.pos):
                    sfx_volume = (event.pos[0] - sfx_slider_rect.x) / sfx_slider_rect.width
                    button_click_sfx.set_volume(sfx_volume)
                    verdict_sfx.set_volume(sfx_volume)
            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:  # Dragging sliders
                if music_slider_rect.collidepoint(event.pos):
                    music_volume = max(0, min(1, (event.pos[0] - music_slider_rect.x) / music_slider_rect.width))
                    pygame.mixer.music.set_volume(music_volume)
                elif sfx_slider_rect.collidepoint(event.pos):
                    sfx_volume = max(0, min(1, (event.pos[0] - sfx_slider_rect.x) / sfx_slider_rect.width))
                    button_click_sfx.set_volume(sfx_volume)
                    verdict_sfx.set_volume(sfx_volume)


# Main game loop
def game_loop():
    global case_index, result_text, dialogue_index, case_finished_time, verdict, current_text, char_index, text_timer, text_speed, evidence_scroll_offset, verdict_timer_start
    running = True
    show_skip_button = True  # Flag to control the visibility of the Skip button

    # Play dialogue music for the first case
    play_music(dialogue_music, loop=True)

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
        
        # Start the timer when the verdict phase begins
        if dialogue_index >= len(case["dialogue"]) and verdict_timer_start is None:
            verdict_timer_start = time.time()  # Start the timer when the verdict phase begins

        # Draw the progress bar if the verdict hasn't been decided
        if verdict is None and dialogue_index >= len(case["dialogue"]):
            draw_progress_bar()
            draw_moral_meter()  # Draw the moral meter above the progress bar

        # Handle time-out condition
        if verdict_timer_start is not None and time.time() - verdict_timer_start > VERDICT_TIME_LIMIT and verdict is None:
            verdict = "timeout"
            result_text = "Time Out"
            case_finished_time = time.time()

        # Draw verdict buttons only if verdict hasn't been given
        if verdict is None and dialogue_index >= len(case["dialogue"]):
            innocent_btn, guilty_btn = draw_verdict_buttons(evidence_bottom_y)

        # Display the result text if the verdict has been decided
        if result_text:
            color = (0, 255, 0) if result_text == "Justice" else (255, 0, 0) if result_text == "Injustice" else GRAY
            result_text_display = font.render(result_text, True, color)
            screen.blit(result_text_display, (screen.get_width() // 2 - result_text_display.get_width() // 2, 600))

        # Draw the Skip button if it should be visible
        if show_skip_button:
            skip_btn = draw_skip_button()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(button_click_sfx)  # Play button click SFX
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(button_click_sfx)  # Play button click SFX
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

        # Draw the custom mouse pointer
        if custom_mouse:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(custom_mouse, (mouse_x, mouse_y))

        pygame.display.flip()

        # Transition to next case after a small delay
        if result_text and case_finished_time and time.time() - case_finished_time > 2:  # Wait for 2 seconds before transitioning
            # Show the truth after the verdict
            show_truth(case)

            # Reset the timer for the next case
            verdict_timer_start = None  # Reset the timer after the truth slide

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

                # Restart dialogue music for the next case
                play_music(dialogue_music)

        pygame.time.Clock().tick(60)


def show_thank_you_message():
    play_music(thank_you_music, loop=False)
    # Display "Thank You For Judging" and the final moral meter score
    end_message = font.render("Thank You For Judging", True, WHITE)
    moral_message = font_title.render(f"Final Moral Score: {moral_meter:.2f}", True, WHITE)
    start_time = time.time()

    # Show the message for 6 seconds
    while time.time() - start_time < 6:
        screen.fill(BLACK)
        screen.blit(end_message, (screen.get_width() // 2 - end_message.get_width() // 2, screen.get_height() // 2 - 50))
        screen.blit(moral_message, (screen.get_width() // 2 - moral_message.get_width() // 2, screen.get_height() // 2 + 50))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Fade out the message
    for alpha in range(255, -1, -5):  # Gradually reduce alpha
        fade_surface = pygame.Surface(screen.get_size())
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Scroll the credits
    credits_text = """
    Music by
    LFC Records from Pixabay
    Shakib Hasan from Pixabay
    Dubush Miaw from Pixabay
    Maksym Dudchyk from Pixabay

    SFX by
    Vlad Krotov from Pixabay
    Lesiakower from Pixabay

    Game Powered By
    Python using PyGame

    Made By
    Infindev

    Fireside Jam 2025
    """
    scroll_credits(credits_text, font_small, screen, scroll_speed=1)

    # A Sweet Final Message At the End
    show_final_message()

def scroll_credits(credits_text, font, screen, scroll_speed=1):
    # Split the credits text into lines
    lines = credits_text.split("\n")
    rendered_lines = [font.render(line, True, WHITE) for line in lines]

    # Calculate the starting Y position (off-screen at the bottom)
    start_y = screen.get_height()

    # Calculate the total height of the credits
    total_height = sum(line.get_height() + 10 for line in rendered_lines)

    # Scroll the credits
    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(BLACK)

        # Draw each line of the credits
        y = start_y
        for line in rendered_lines:
            x = (screen.get_width() - line.get_width()) // 2  # Center horizontally
            screen.blit(line, (x, y))
            y += line.get_height() + 10

        # Update the starting Y position
        start_y -= scroll_speed

        # Stop scrolling when the credits are off-screen
        if start_y + total_height < 0:
            running = False

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS


def show_final_message():
    message = "Thank You For Playing"
    fade_duration = 1.0  # Duration for fade-in and fade-out (in seconds)
    hold_duration = 3.0  # Duration to hold the message at full opacity (in seconds)
    total_duration = fade_duration * 2 + hold_duration
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed > total_duration:
            break

        screen.fill(BLACK)

        # Compute alpha for fade-in, hold, and fade-out
        if elapsed < fade_duration:
            alpha = int(255 * (elapsed / fade_duration))  # Fade in
        elif elapsed < fade_duration + hold_duration:
            alpha = 255  # Hold full opacity
        else:
            alpha = int(255 * (1 - (elapsed - fade_duration - hold_duration) / fade_duration))  # Fade out

        # Render the message
        message_surface = font_title.render(message, True, WHITE)
        message_surface.set_alpha(alpha)

        # Center the message on the screen
        x_center = (screen.get_width() - message_surface.get_width()) // 2
        y_center = (screen.get_height() - message_surface.get_height()) // 2
        screen.blit(message_surface, (x_center, y_center))

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit to 60 FPS

async def main():
    # Show the title screen
    show_title_screen()

    # Start the game
    game_loop()

    # Quit pygame
    pygame.quit()
    await asyncio.sleep(0)

asyncio.run(main())