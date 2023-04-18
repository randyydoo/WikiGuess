var score = 0;

document.getElementById("start").addEventListener("click", function() {
  fetch("/get_text")
    .then(response => response.json())
    .then(data => {
      newText(data);
    })
    .catch(error => console.error(error));
});

document.getElementById('left_button').addEventListener('click', function() {
  var value = document.getElementById('left_button').value;
  if (value === 'gpt') {
    score++;
  } else {
    score = 0;
  }
  document.getElementById('score').innerHTML = 'Score: ' + score;
});

document.getElementById('right_button').addEventListener('click', function() {
  var value = document.getElementById('right_button').value;
  if (value === 'gpt') {
    score++;
  } else {
    score = 0;
  }
  document.getElementById('score').innerHTML = 'Score: ' + score;
});

// Function to set text for left and right buttons
function newText(data) {
  fetc
  var wiki_text = data['Wiki'];
  var gpt_text = data['Gpt'];
  var random = data['Num'];
  var sport = data['Sport'];
  document.getElementById('left_button').style.display = "block";
  document.getElementById('right_button').style.display = "block";

  // Use the retrieved variable in your HTML
  document.getElementById('score').innerHTML = 'Score: ' + score;
  if (random == 1) {
    document.getElementById('left_button').innerHTML = wiki_text;
    document.getElementById('left_button').value = 'wiki';
    document.getElementById('left_sport').innerHTML = sport;

    document.getElementById('right_button').innerHTML = gpt_text;
    document.getElementById('right_button').value = 'gpt';
    document.getElementById('right_sport').innerHTML = sport;
  } else {
    document.getElementById('right_button').innerHTML = wiki_text;
    document.getElementById('right_button').value = 'wiki';
    document.getElementById('right_sport').innerHTML = sport;

    document.getElementById('left_button').innerHTML = gpt_text;
    document.getElementById('left_button').value = 'gpt';
    document.getElementById('left_sport').innerHTML = sport;
  }
}







