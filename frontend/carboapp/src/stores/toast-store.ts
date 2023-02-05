import { writable } from 'svelte/store';
import ToastModel from '../models/toast/toast-model';

export const toasts = writable<ToastModel[]>([]);


export function displayToast(message: string, color: string, time: number){
    const toastItem = new ToastModel(color, time, message);

    toasts.update(current => [toastItem, ...current])
    
    setTimeout(() => {       
        toasts.update(current => {
            const last = current.length - 1
            return current.filter((_, index) => index !== last)
        })
    }, time)
}