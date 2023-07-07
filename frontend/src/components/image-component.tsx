import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const userId = "testing";
const socket = io(`http://localhost:5000/chat${userId}`);

const ImageComponent = () => {
    const [imageBlobLink, setImageBlobLink] = useState('');

    useEffect(() => {
        socket.on('imageBlobLink', (link: string) => {
            setImageBlobLink(link);
        });

        // On initial load, request the image link from the server
        socket.emit('getImageBlobLink');
    }, []);

    return (
        <div>
            <img src={imageBlobLink} alt="Image" />
        </div>
    );
};

export default ImageComponent;
