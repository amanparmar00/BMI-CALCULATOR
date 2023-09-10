function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value) / 100; // Convert cm to meters
    
    if (isNaN(weight) || isNaN(height) || height === 0) {
        document.getElementById('result').innerText = "Please enter valid values.";
        return;
    }
    
    const bmi = weight / (height * height);
    const result = `Your BMI is ${bmi.toFixed(2)}.`;
    document.getElementById('result').innerText = result;
}
