import { goto } from '$app/navigation';
import { writable } from 'svelte/store';
import type UserModel from '../models/user/user-model';
import { displayToast } from './toast-store';

export const user = writable<UserModel | undefined>();


export function logout(){
    localStorage.removeItem('usertoken');

    user.update(() => undefined);

    goto('/', {replaceState: true})

    displayToast('Desconectado!', '#28a745', 4000);
}