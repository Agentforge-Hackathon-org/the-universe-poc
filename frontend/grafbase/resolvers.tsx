import { Resolvers } from '@apollo/client'

const resolvers: Resolvers = {
    Message: {
        // The resolvers for the fields of the Message type
        username: (message) => message.username,
        avatar: (message) => message.avatar,
        body: (message) => message.body,
        likes: (message) => message.likes,
        dislikes: (message) => message.dislikes,
        timestamp: (message) => message.timestamp,
    },
};

export default resolvers;
