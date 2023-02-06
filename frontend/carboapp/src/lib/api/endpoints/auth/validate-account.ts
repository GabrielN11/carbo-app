import { apiPut } from "$lib/api/api";
import type { SuccessfullyResponse} from "$lib/api/api-models";
import type UserModel from "../../../../models/user/user-model";
import type UserValidationModel from "../../../../models/user/user-validation-model";

export default async function validateAccount(model: UserValidationModel): Promise<SuccessfullyResponse<UserModel>> {
    const res = await apiPut<SuccessfullyResponse<UserModel>, UserValidationModel>(`/sign-up`, model, false)

    return res
}