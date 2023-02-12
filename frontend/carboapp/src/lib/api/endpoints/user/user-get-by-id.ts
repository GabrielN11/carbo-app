import { apiGet } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";

export default async function getUserById(id: number): Promise<SuccessfullyResponse<UserModel>>{
    const user = await apiGet<SuccessfullyResponse<UserModel>>(`/user/${id}`, false)
    return user
}