export interface Usage {
    prompt_tokens: number;
    completion_tokens: number;
    total_tokens: number;
}

export interface Content {
    text?: string;
    index?: number;
    imageUrl?: string;
    base64Image?: string;
}

export interface AIResponse {
    id: string;
    mode: string;
    role: string;
    created: string;
    content: Content;
    usage?: Usage;
    viewerContent?: boolean;
    object?: string;
}

export interface Prompt {
    mode: string;
    model: string;
    prompts: string[];
    imageUrl?: string;
    base64Image?: string;
    n?: number;
    size?: string;
    timestamp?: string;
}