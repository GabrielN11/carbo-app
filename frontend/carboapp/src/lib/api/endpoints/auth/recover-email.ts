import { apiPost } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";
import type UserLoginModel from "../../../../models/user/user-login-model";
import type UserEmailModel from "../../../../models/user/user-email-model";

interface UserId{
    id: number;
}

export default async function recoverEmail(model: UserEmailModel): Promise<SuccessfullyResponse<UserId>> {
    const res = await apiPost<SuccessfullyResponse<UserId>, UserEmailModel>('/recovery', model, false)

    return res
}