import express from 'express';
import { ApolloServer } from 'apollo-server-express';
import { ApolloClient, InMemoryCache } from '@apollo/client';
import { createServer } from 'http';
import { Request } from 'express';
import { gql } from '@apollo/client';
import cors from 'cors';
import io from 'socket.io-client';


// Import your GraphQL schema and resolvers
const typeDefs = require('grafbase/schema');
const resolvers = require('grafbase/resolvers');

const app = express();
app.use(cors());

const server = new ApolloServer({
    typeDefs,
    resolvers,
});

server.applyMiddleware({ app });

const httpServer = createServer(app);

// Set up WebSocket connection
const socket = io('http://localhost:5000/chat');

// When the chat window message list is updated, send the new message
function sendMessage(message: Request) {
    socket.emit('newMessage', message);

    app.post('/chat', (req, res) => {
        const { payload } = req.body;
        res.json({ payload });
    });
}

httpServer.listen({ port: 5000 }, () => {
    console.log(`🚀 Server ready at http://localhost:5000${server.graphqlPath}`);
})

httpServer.on('connection', (socket) => {
    socket.on('newMessage', (message) => {
        sendMessage(message);
    });
})
