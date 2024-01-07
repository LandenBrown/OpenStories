from openai import OpenAI
import easygui
import time
debugMode = False

##paste your own API key here
#If you don't have one create a Premium OpenAI account and get one. Beware of rate limits. We can likely tune this better to avoid rate limit exhaustion. 
my_apiKey = ""
#Paste the path you want the story files to be created at.
#e.g: C:\Users\Bob\Desktop
#Note: Do not remove the lonesome 'r' infront of the string. This is 'r' tells Python to treat the path as a raw string, which ignores escape characters.
localPath = r""




client = OpenAI(api_key=my_apiKey)
print("Give me some details about the world setting you'd like to create")
settingInput = easygui.enterbox("Give me some details about the world you would like to create for your story...")
print("Got it...")
readingLevelInput = easygui.enterbox("What reading grade reading level would you like me to write this story in? (e.g. 5th, 8th, college)")
print("Sounds great!")
fantasyOrReal = easygui.buttonbox("Will this be a fantasy setting or a realistic setting?", choices=["Fantasy", "Realistic"])

def checkError(r):
    print("Run status: " + r.status)
    if r.status == "failed":
            print("world status generate failed")
            print(r.last_error.code)
            print(r.last_error.message)
            exit()

def CreateWorldSetting(): 
    #Using premade Assistant - World Setting Creator
    CreatedAssistant_id = "asst_CYNpsPk15iNBbK8PZiDH9J9W"


    #thread creation
    thread = client.beta.threads.create()
    #print(thread)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=settingInput
    )
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="I want you to create this in a " + fantasyOrReal + " setting"
    )

    #print(message)

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating World Setting....")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\WorldSetting.rtf", "w")
    f.write(returnedMessage)
    f.close()

    print("FINISHED GENERATING WORLD SETTING.......")

######################

def GenerateStoryCharacters():
    f = open(localPath+"\WorldSetting.rtf", "r")
    worldSetting = f.read()
    f.close()

    CreatedAssistant_id = "asst_GgyZOfWrB541GJitGfdJnUtb"

    #thread creation
    thread = client.beta.threads.create()
    #print(thread)



    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=worldSetting
    )
    

    #print(message)

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating story characters...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\StoryCharacters.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING STORY CHARACTERS.......")


def GenerateStoryOutline():
    f = open(localPath+"\WorldSetting.rtf", "r")
    worldSetting = f.read()
    f.close
    f = open(localPath+"\StoryCharacters.rtf", "r")
    storyCharacters = f.read()
    f.close

    combinedContext = worldSetting + "\n" + storyCharacters

    CreatedAssistant_id = "asst_uRd58SlzofPGRGvvamMuTODP"

    #thread creation
    thread = client.beta.threads.create()
    #print(thread)


    #Send World Setting
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=worldSetting
    )
    
    #Send Story Characters
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=storyCharacters
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating story outline...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\StoryOutline.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING STORY OUTLINE.......")




def GenerateStoryChapters():
    f = open(localPath+"\WorldSetting.rtf", "r")
    worldSetting = f.read()
    f.close
    f = open(localPath+"\StoryCharacters.rtf", "r")
    storyCharacters = f.read()
    f.close
    f = open(localPath+"\StoryOutline.rtf", "r")
    storyOutline = f.read()
    f.close

    CreatedAssistant_id = "asst_w3pbxgYNEZciSD46HaIZ8ihq"

    #thread creation
    thread = client.beta.threads.create()
    #print(thread)


    #Send World Setting
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=worldSetting
    )
    
    #Send Story Characters
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=storyCharacters
    )
    #Send Story Outline
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=storyOutline
    )
    #Send Reading Level
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Write this story at a " + readingLevelInput + " grade reading level"
    )

    
    #Generate Chapter 1
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Generate Chapter 1"
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating chapter 1...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\Chapter1.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING CHAPTER 1.......")
    ########################### GENERATE SECOND CHAPTER #######################

    #Generate Chapter 2
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Generate Chapter 2"
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating chapter 2...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\Chapter2.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING CHAPTER 2.......")

    ########################### GENERATE THIRD CHAPTER #######################

    #Generate Chapter 3
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Generate Chapter 3"
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating chapter 3...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\Chapter3.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING CHAPTER 3.......")
    ########################### GENERATE FOURTH CHAPTER #######################

    #Generate Chapter 3
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Generate Chapter 4"
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating chapter 4...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\Chapter4.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING CHAPTER 4.......")
    ########################### GENERATE FIFTH CHAPTER #######################

    #Generate Chapter 3
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Generate Chapter 5"
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=CreatedAssistant_id,
    )

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run.status != "completed":
        time.sleep(2)
        print("Generating chapter 5...")
        run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
        )
        checkError(run)

    #print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    returnedMessage = ""
    for message in reversed(messages.data):
        #print(message.content[0].text.value)
        returnedMessage = message.content[0].text.value

    f = open(localPath+"\Chapter5.rtf", "w")
    f.write(returnedMessage)
    f.close()
    print("FINISHED GENERATING CHAPTER 5.......")

    ##### RUN PROGRAM #####

if debugMode == False:
    CreateWorldSetting()
    GenerateStoryCharacters()
    GenerateStoryOutline()
    GenerateStoryChapters()
else:
    easygui.msgbox(msg = "Debug Mode on, Skipping Run", title="Debug Mode On", ok_button="OK")