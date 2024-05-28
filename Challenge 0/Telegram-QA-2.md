Question_1: Do we need to scaffold-eth install again to start each project?
Answer_1: Yeah, each project will have it's own local directory where you will need to 'yarn install'

Question_2: My automated tests passes but when I try to deploy using vercel & submit the link to the portal - the submission fails :(
Answer_2: If you mouse over the '?' on your profile submission, there will be more info there about why it failed.
Question_2b: yeah it's literally those same tests that passes locally!
Answer_2b: Are you sure you're entering the correct address in the URL for the entry?  Looks like it's trying to grab your contract and can't find it. Although, it would usually tell you something about that in the initial error.
Question_2c: yup tried it again but same result
Answer_2c: Looks like the grader is acting up a bit, so if you get an error like seen above when submitting, hold tight! So a workaround for this issue is to use Goerli instead of Sepolia.  I know it's deprecated, but it's still working fine while something is up with Sepolia

Question_3: Question, how to deploy the project as another name? I already deployed but  I hope deploy as another url.
Answer_3: If you used vercel you can go to your deploy > Project Settings > Domains. There you can add another .vercel.app domain.

Question_4: I was running into errors to when I started so every project I had to use yarn set version canary and it works with that
Answer_4: Yeah I would make sure you’re using yarn v2 and clean it out and clone again.

Question_5: Anyone ever restarted the project and the repo doesn’t clone ?
Answer_5: Resolved this issue, GitHub my shell kept running insurance of other branch

Question_6: I'm getting errors with yarn install. The error that i'm getting is in the link step and its this:

 YN0000:  Link step
 YN0007:  se-2@workspace:. must be built because it never has been before or the last one failed
 YN0009:  se-2@workspace:. couldn't be built successfully (exit code 1, logs can be found here:

and upon checking the build.log this 
# This file contains the result of Yarn building a package (se-2@workspace:.)
# Script name: postinstall
husky - .git can't be found
Answer_6: It may be related to the yarn version. You can try: yarn set version canary and then yarn install

Question_7: Hi friends, I am trying to redo my exercise to refresh my memory, but I can’t get the burner wallet address on the to right corner of the localhost page. Should I delete the project directory and reinitiate one?
Answer_7: If your front end is pointing to a network that isn't hardhat, the burner wallet won't be an option.  Did you start this run through with a fresh clone?. If not, I do recommend it for this challenge.

Question_8: Can someone help me with this? How can I get gas?
Answer_8: You can get gas here: https://sepoliafaucet.com or here https://www.infura.io/faucet/sepolia. They are the official sites recommended in the challenge. Infura also works if u cant wait 24 hours for the faucet to cool down and already spent ur 0.5 sepolia

Question_9: when I am setting the environment, my terminal shows this:

'''
C:\Windows\system32>git clone https://github.com/scaffold-eth/se-2-challenges.git challenge-0-simple-nft
Cloning into 'challenge-0-simple-nft'...
fatal: unable to access 'https://github.com/scaffold-eth/se-2-challenges.git/': Recv failure: Connection was reset
'''

What should I do with it?
Answer_9: The error message "Recv failure: Connection was reset" often indicates a network issue during the Git clone operation. Here are a few steps you can take to troubleshoot and resolve the problem:

1. Check Internet Connection:
   - Ensure that your internet connection is stable. Try accessing other websites or resources to confirm.

2. Firewall or Antivirus Blocking:
   - Check if your firewall or antivirus software is blocking the Git connection. Temporarily disable them and try cloning the repository again.

3. Use SSH Instead of HTTPS:
   - If you have set up SSH keys, consider using the SSH URL for cloning instead of HTTPS. Change the clone command to:
    
     git clone git@github.com:scaffold-eth/se-2-challenges.git challenge-0-simple-nft
     
4. Retry the Clone:
   - Sometimes, network issues can be transient. Retry the clone command after a short period.

5. Use a Git Credential Manager:
   - If you are on Windows, consider using a Git credential manager. GitHub recommends using the Git Credential Manager for Windows. You can download and install it from [here](https://github.com/microsoft/Git-Credential-Manager-for-Windows).

6. Git Config Settings:
   - Check your Git configuration settings. Ensure that your username and email are correctly set.
    
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     
7. HTTPS vs. SSH Authentication:
   - If you are using HTTPS, make sure you have the correct credentials (username and password or a personal access token). If you are using SSH, make sure your SSH key is correctly configured.

After trying these steps, you should be able to clone the repository successfully. If the issue persists, it might be worth checking with your network administrator or GitHub support for further assistance.

Question_10: please when i run yarn vercel, i get this error; Error: No Next.js version could be detected in your project. Make sure `"next"` is installed in "dependencies" or "devDependencies"
Answer_10: The error you're encountering with yarn vercel is because Vercel couldn't detect a Next.js version in your project. To resolve this issue, follow these steps:

1. Ensure that Next.js is installed in your project's dependencies or devDependencies. You can install it using Yarn with the following command: yarn add next

2. Double-check your package.json file to make sure that Next.js is listed in either dependencies or devDependencies. If it's missing, add it manually and then run the yarn vercel command again.

3. If you're still facing issues, make sure you're in the correct directory where your Next.js project is located before running yarn vercel.

4. Verify that your package.json and yarn.lock files are up to date and correctly reflect your project's dependencies.

5. If you've recently added Next.js as a dependency, make sure to commit the changes to your version control system (e.g., Git) before deploying to Vercel.

Once you've ensured that Next.js is correctly installed and configured in your project, try running yarn vercel again, and the error should be resolved.

Question_11: In the Speedrunethereum Checkpoint 0, the code for the NFT and the frontend are all written and done. What exactly am I gonna be doing as the task? Just changing the network ? Or do I rewrite the NFT smart contract or sth
Answer_11: As far as coding goes, yes just changing the network.  This one is more about getting the environment going and learning the steps to start up your chain, front end, and deploy a contract

Question_12:  I try to run "yarn vercel" I got lot of errors: "ReferenceError: document is not defined".
Answer_12: Found the solution in another post  " just remove "caret" from ‘next’ version and try again "yarn vercel" hopefully it should work

