export interface SuccessfullyResponse<T>{
    message: string;
    data: T;
}

export interface SuccessfullyListResponse<T>{
    message: string;
    data: Array<T>;
}

export interface SuccessfullyMessageResponse{
    message: string;
}

export interface ErrorResponse{
    error: string;
}