const CodeSnippets = [
"How many programmers does it take to change a light bulb?\nNone, that's a hardware problem!",

"I HATE PROGRAMMING\nI HATE PROGRAMMING\nI HATE PROGRAMMING\nIT WORKS!\nI LOVE PROGRAMMING",

"YOU ARE THE {CSS} TO MY &lt;/HTML&gt;",

"YOU ARE THE {CSS} TO MY &lt;/HTML&gt;, {JS} TO MY WEBPAGE",

"Why do programmers prefer dark mode?\nBecause light attracts bugs, and they're trying to keep things bug-free!",

"How do you comfort a JavaScript bug?\nYou console it!",

'for charming_smile in room:\n    exhibit(charming_smile)\n    say("Are you a function? Because you make my heart return true.")',

'for charming_smile in room:\n    exhibit(charming_smile)\n    say("Are you a function? Because you make my heart return true.")',

'if captivating():\n    express_interest()\n    whisper("Are you CSS? Because you\'re making everything look better.")',

'while not_offended():\n    share_dark_joke()\n    chuckle_sarcastically()',

'for twisted_mind in audience:\n    appreciate_dark_humor(twisted_mind)\n    say("I used to play piano by ear, but now I use my hands.")',

'while not_shattered():\n    code_dark_humor()\n    say("I named my hard drive \'dat_ass\' so once a month, my computer asks if I want to back \'dat_ass\' up.")',

'def catch_feelings():\n    feelings = []\n    while True:\n        try:\n            feelings.append("Love")\n            print("Caught a feeling! Current feelings:", feelings)\n        except Exception as e:\n            print("Error:", e)\n            break\ncatch_feelings()\n#I wrote a function to catch feelings, but I always end up in an infinite loop.',

'Why do programmers always mix up Christmas and Halloween?\nBecause Oct 31 == Dec 25 !',

'Why did the software developer go broke?\nBecause they used up all their cache flow.',

'                (code):\nWhile T̶h̶e̶r̶e̶\'̶s̶  ̶L̶i̶f̶e̶,\nT̶h̶e̶r̶e̶\'̶s̶ ̶H̶o̶p̶e̶        \nprint(Bug)\nM̶a̶r̶c̶u̶s̶ ̶T̶u̶l̶l̶i̶s̶ ̶C̶i̶c̶e̶r̶e̶\n#~Confusedprogrammer'
];

document.getElementById('Popup-trigger').addEventListener('click', function() {
    const randomIndex = Math.floor(Math.random() * CodeSnippets.length);
    const randomHTML = CodeSnippets[randomIndex];

    // Set the HTML content for the code snippet container
    document.getElementById('Dynamic-code').innerHTML = randomHTML;

    // Display the popup and code snippet
    document.getElementById('Html-popup').style.display = 'block';
});