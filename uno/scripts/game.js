document.body.onload = displayPlayers;

function displayPlayers() {
  // create a new div element
  var newDiv = document.createElement('div');
  // and give it some content
  var newContent = document.createTextNode('Hi there and greetings!');
  // add the text node to the newly created div
  newDiv.appendChild(newContent);

  // add the newly created element and its content into the DOM
  var currentDiv = document.getElementById('players');
  document.body.insertBefore(newDiv, currentDiv);
}

function Hello() {
  alert('Hello, World');
}