import { useState } from "react";
import useSound from "use-sound";
import io from 'socket.io-client'

const userid = "testingName"

const socket = io(`http://localhost:5000/chat${userid}`);

export const NewMessageForm = () => {
  const [play] = useSound("sent.wav");
  const [body, setBody] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (body) {
      socket.emit('newMessage', {
        body,
      });
      play();
      setBody('');
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex items-center space-x-3">
      <input
        autoFocus
        id="message"
        name="message"
        placeholder="Write a message..."
        value={body}
        onChange={(e) => setBody(e.target.value)}
        className="flex-1 h-12 px-3 rounded bg-[#222226] border border-[#222226] focus:border-[#222226] focus:outline-none text-white placeholder-white"
      />
      <button
        type="submit"
        className="bg-[#222226] rounded h-12 font-medium text-white w-24 text-lg border border-transparent hover:bg-[#363739] transition"
        disabled={!body}
      >
        Send
      </button>
    </form>
  );
};