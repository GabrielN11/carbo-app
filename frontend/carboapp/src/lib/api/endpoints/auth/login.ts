import { apiPost } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";
import type UserLoginModel from "../../../../models/user/user-login-model";

export default async function signIn(model: UserLoginModel): Promise<SuccessfullyResponse<UserModel>> {
    const user = await apiPost<SuccessfullyResponse<UserModel>, UserLoginModel>('/sign-in', model, false)

    return user
}