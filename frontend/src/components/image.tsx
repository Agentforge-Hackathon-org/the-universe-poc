import Image, { ImageProps } from 'next/image';

interface ImageComponentProps extends ImageProps {
    // Add any additional props you need
}

const ImageComponent: React.FC<ImageComponentProps> = ({ src, alt, width, height, ...props }) => {
    return (
        <Image src={src} alt={alt} width={width} height={height} {...props} />
    );
};

export default ImageComponent;
