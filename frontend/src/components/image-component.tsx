import React, { useEffect, useState } from 'react';
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

const ImageComponent: React.FC = () => {
    const [imageBlobLink, setImageBlobLink] = useState<string>('https://oaidalleapiprodscus.blob.core.windows.net/private/org-kOlvtpZHBKbfNHc1yK9laSY9/user-yB15XXARpR9bSbwdGriqO5ps/img-tIp8L7gRgxCgHQ5zp5n9cvuk.png?st=2023-07-03T10%3A44%3A44Z&se=2023-07-03T12%3A44%3A44Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-07-03T06%3A45%3A52Z&ske=2023-07-04T06%3A45%3A52Z&sks=b&skv=2021-08-06&sig=p39mK6cAEJQDb7ZgAAOu/OCKGUAOWXRmWnwi9YVcJY4%3D');
    useEffect(() => {
        const client = new ApolloClient({
            uri: 'localhost:3000/updateImage',
            cache: new InMemoryCache(),
        });

        client
            .query({
                query: gql`
          query GetImageBlobLink {
            imageBlobLink
          }
        `,
            })
            .then((response) => {
                const { imageBlobLink } = response.data;
                setImageBlobLink(imageBlobLink);
            })
            .catch((error) => console.error(error));
    }, []);

    return (
        <div>
            <img
                src={imageBlobLink}
                alt="Image"
            />
        </div>
    );
};

export default ImageComponent;
