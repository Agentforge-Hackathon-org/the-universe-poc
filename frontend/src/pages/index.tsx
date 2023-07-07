import { useSession } from "next-auth/react";

import { Header } from "@/components/header";
import { MessageList } from "@/components/message-list";
import { NewMessageForm } from "@/components/new-message-form";
import ImageComponent from "@/components/image-component";

export default function Home() {

  return (
    <div className="flex flex-col bg-cover">
      <Header />
        <>
          <div className="flex-1 overflow-y-scroll no-scrollbar p-6">
            <div className="max-w-4xl mx-auto">
              <div className="flex justify-between items-center">
                <ImageComponent />
                <MessageList />
              </div>
            </div>
          </div>
          <div className="p-6 bg-white/5 border-t border-[#363739]">
            <div className="max-w-4xl mx-auto">
              <NewMessageForm />
            </div>
          </div>
        </>
        <div className="h-full flex items-center justify-center flex-col space-y-2.5">
            <>
             <p>

              </p>
            </>
        </div>
    </div>
  );
}
