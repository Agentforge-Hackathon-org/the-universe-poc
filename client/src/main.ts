import bot from './assets/bot.png';
import user from './assets/user.png';

const username = 'user1';

const form = document.querySelector('form');
const chatContainer = document.getElementById('chat-container')

let ws: WebSocket

if (chatContainer === null) {
  throw new Error('chatContainer is null');
}

if (form === null) {
  throw new Error('form is null');
}
ws = new WebSocket(`ws://localhost:8000/chat/${username}`);

let loadInterval:any

//loading animation for the bot
function loader(element: HTMLElement) {
  element.textContent = '';
  loadInterval = setInterval(() => {
    element.textContent += '.';

    if (element.textContent === '....') {
      element.textContent = '';
    }
  }, 300)
}

// typewriter effect on bot message
function typeText(element: HTMLElement, text: string) {
  let index = 0;

  let interval = setInterval(() => {
    if (index < text.length) {
      element.innerHTML += text.charAt(index);
      index++;

    } else {

      clearInterval(interval);
    }
  })
}

// create unique id for each user
function generateUniqueId() {
  const timestamp = Date.now();
  const randomNumber = Math.random();
  const hexadecimalString = randomNumber.toString(16);

  return `id-${timestamp}-${hexadecimalString}`;
}

// insert user profile and message in div
function chatStripe(isAi: boolean, value: string, uniqueId?: string) {
  return (
    `
  <div class="wrapper ${isAi && 'ai'}">
    <div class="chat">
      <div class="profile">
        <img
          src="${isAi ? bot : user}"
          alt="${isAi ? 'bot' : 'user'}"
          />
      </div>
      <div class="message" id="${uniqueId}">${value}</div>
    </div>
  </div>
  `
  )
}



// Save conversation to a file
function saveToFile(filename: string, text: string) {
  const element = document.createElement("a");
  element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
  element.setAttribute("download", filename);
  element.style.display = "none";
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}

//get conversation history
const conversationHistory = Array.from(document.querySelectorAll('.message'))
  .map((message) => message.textContent)
  .join('');


ws.send(JSON.stringify({
  prompt: data.get('prompt'),
  context: conversationHistory
}));

clearInterval(loadInterval);
messageDiv.innerHTML = '';


const parsedData = await response.text();
console.log(parsedData);
const responseObj = JSON.parse(parsedData);
const {content} = responseObj.bot;

form.addEventListener('submit', handleSubmit);
form.addEventListener('keyup', (event) => {
  if (event.key === 'Enter') {
    handleSubmit(event);
  }
});
// Establish WebSocket connection
ws = new WebSocket('ws://localhost:8000/chat/user1');
// Handle WebSocket events
ws.addEventListener('open', handleWebSocketOpen);
ws.addEventListener('message', (event) => handleMessage(event.data));
ws.addEventListener('close', handleWebSocketClose);