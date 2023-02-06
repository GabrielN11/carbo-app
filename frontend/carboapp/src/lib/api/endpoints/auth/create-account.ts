import { apiPost } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";
import type UserLoginModel from "../../../../models/user/user-login-model";
import type UserCreateModel from "../../../../models/user/user-create-model";

interface UserId{
    id: number;
}

export default async function createAccount(model: UserCreateModel): Promise<SuccessfullyResponse<UserId>> {
    const user = await apiPost<SuccessfullyResponse<UserId>, UserCreateModel>('/sign-up', model, false)

    return user
}