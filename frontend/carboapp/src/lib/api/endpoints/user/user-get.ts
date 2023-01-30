import { apiGet } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";

const baseUrl = 'http://127.0.0.1:5000'

export default async function getUser(): Promise<SuccessfullyResponse<UserModel>>{
    const user = await apiGet<SuccessfullyResponse<UserModel>>(baseUrl + '/sign-in', true)
    debugger
    return user
}