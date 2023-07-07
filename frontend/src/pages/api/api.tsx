import express from 'express';

import cors from 'cors';

import io from 'socket.io-client';

const app = express();

app.use(cors());

const userid = "testingName"

const socket = io(`http://localhost:5000/chat${userid}`);

function sendMessage(message: Request) {
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    })
}
socket.on('newMessage', (message) => {
    sendMessage(message)
});
