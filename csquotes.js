const codeSnippets = [
'if sad():\n    stop(sad())\n    be_awesome()',

'if problems_exist():\n    solve(problems)\nelse:\n    celebrate()',

'mood = "productive"\nif mood == "productive":\n    code()\nelse:\n    procrastinate()',

'for i in range(len(motivation)):\n    code()',

'try:\n    understand_code()\nexcept Confusion:\n    seek_help()',

'if life.is_busy():\n    prioritize()\n    find_balance()',

'while not perfect():\n    iterate()\n    learn()',
'try:\n    live()\nexcept LifeChallenges:\n    overcome()',

'if dreams:\n    pursue(dreams)\nelse:\n    find_passion()',

'for day in life:\n    make_it_count(day)',

'if not happy():\n    refactor(life)\n    find_joy()',
'if in_doubt():\n    ask_questions()\n    seek_answers()',

'if relationships.empty():\n    build_connections()\nelse:\n    nurture_relationships()',

'try:\n    embrace_change()\nexcept Fear:\n    face_it()',

'if opportunity.exists():\n    seize(opportunity)\nelse:\n    create(opportunity)',
];

document.getElementById('popup-trigger').addEventListener('click', function() {
    const randomIndex = Math.floor(Math.random() * codeSnippets.length);
    const randomHTML = codeSnippets[randomIndex];

    // Set the HTML content for the code snippet container
    document.getElementById('dynamic-code').innerHTML = randomHTML;

    // Display the popup and code snippet
    document.getElementById('html-popup').style.display = 'block';
});