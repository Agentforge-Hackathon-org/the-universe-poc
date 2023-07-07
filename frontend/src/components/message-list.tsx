import { useEffect, useState } from "react";
import { useInView } from "react-intersection-observer";
import { Message } from "@/components/message";
import io from 'socket.io-client'

const userid = "testingName"

const socket = io(`http://localhost:5000/chat${userid}`);

export const MessageList = () => {

  const [scrollRef, inView, entry] = useInView({
    trackVisibility: true,
    delay: 1000,
  });
  const [messages, setMessages] = useState<any[]>([]);

  useEffect(() => {
    socket.on('newMessage', (message) => {
      setMessages(prev => [...prev, message]);
    });

    // On initial load, request latest messages from the server
    socket.emit('getRecentMessages', { last: 100 });
  }, []);

  useEffect(() => {
    if (entry?.target) {
      entry.target.scrollIntoView({ behavior: "smooth", block: "end" });
    }
  }, [messages.length, entry?.target]);

  if (!messages.length) {
    return (
      <div className="flex items-center justify-center h-full">
        <p className="text-white">Fetching chat history.</p>
      </div>
    );
  }

  return (
    <div className="flex flex-col w-full space-y-3 overflow-y-scroll no-scrollbar">
      {!inView && messages.length > 0 && (
        <button onClick={() => entry?.target.scrollIntoView({ behavior: "smooth", block: "end" })}>
          Scroll to see latest messages
        </button>
      )}
      {messages.map(message => (
        <Message key={message.id} message={message} />
      ))}
      <div ref={scrollRef} />
    </div>
  );
};
