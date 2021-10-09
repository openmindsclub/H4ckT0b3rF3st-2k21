# Autotyper

### 1. Description :
Autotyper is a script made by OpenMindsClub to beat the speed typing challenge on : [Typing Speed Test](https://cpstest.org/typing-speed-test/). </br>
This script is only a prototype so we need your help to finish the project !</br>
### 2. How Does it Work : 
### Requirements:
- Python3 : 
 ``` 
 $ sudo apt-get update  
$ sudo apt-get install python3.6 
  ```
- Pynput :
```
$ pip install pynput
```
### How to run the script:
1.  Go to [Typing Speed Test](https://cpstest.org/typing-speed-test/).

2. take the code of the the text that you  need to type and copy it.
- ##### Step 1:<br>
![Step 1 ](https://www.pixenli.com/image/lvyEss24)
- ##### Step 2 :<br>
![Step 3 ](https://www.pixenli.com/image/NxRY-qwG)<br>
3. Paste it in the variable `S` example : 
```
S = "<section id="word-section"><span class="current-word">you</span><span>appear</span> . . ."
``` 

4. using any image editing software take a screenshot and get the coordinations of the typing box then Run the script : <br>
```
$ python Autotyper X Y
```
### 3. Tasks :
As you see the script is lacking a lot of features to be usable, and this is what we need you to help us achieve !</br>
1. Use web scraping to locate the typing box 
2. Use web scraping to get the words that you need to type
3. Reach 100 WPM (words per minute)