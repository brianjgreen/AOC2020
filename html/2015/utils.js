// utils.js
function runSolver(mathLogicFunc, resultId1, resultId2) {
    const input = document.getElementById('inputData').value.trim();
    const resultsArea = document.getElementById('resultsArea');
    const part1Display = document.getElementById(resultId1);
    const part2Display = document.getElementById(resultId2);

    if (!input) {
        alert("Please paste some input first!");
        return;
    }

    // Execute the math logic passed from the specific day file
    const results = mathLogicFunc(input);

    // Update the UI
    part1Display.textContent = results.p1;
    part2Display.textContent = results.p2;
    resultsArea.style.display = 'block';
}
