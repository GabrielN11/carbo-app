import { apiGet } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserProfileModel from "../../../../models/user/user-profile-model";

export default async function getUserById(id: number): Promise<SuccessfullyResponse<UserProfileModel>>{
    const user = await apiGet<SuccessfullyResponse<UserProfileModel>>(`/user/${id}`, false)
    return user
}