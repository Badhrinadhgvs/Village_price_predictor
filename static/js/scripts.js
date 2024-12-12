// Add dynamic greeting and smooth hover animations
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('h1');
  const hour = new Date().getHours();
  let greeting = '';

  if (hour < 12) {
    greeting = '🌅 Good Morning!';
  } else if (hour < 18) {
    greeting = '🌞 Good Afternoon!';
  } else {
    greeting = '🌙 Good Evening!';
  }

  header.innerHTML = `${greeting} Welcome to the <br> <strong>Village Price Predictor</strong>`;
});

// Highlight expensive predicted prices
document.addEventListener('DOMContentLoaded', () => {
  const predictedPriceElement = document.querySelector('.predicted-price');
  const price = parseFloat(predictedPriceElement.textContent.replace('$', ''));

  if (price > 100) {
    predictedPriceElement.style.background = 'linear-gradient(45deg, #ff758c, #ff9a9e)';
    predictedPriceElement.style.color = 'white';
  } else {
    predictedPriceElement.style.background = 'linear-gradient(45deg, #a8e063, #56ab2f)';
    predictedPriceElement.style.color = 'white';
  }
});
