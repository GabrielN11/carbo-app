import { apiPut } from "$lib/api/api";
import type { SuccessfullyMessageResponse} from "$lib/api/api-models";
import type UserPasswordModel from "../../../../models/user/user-password-model";

export default async function changePassword(model: UserPasswordModel, id: number): Promise<SuccessfullyMessageResponse> {
    const res = await apiPut<SuccessfullyMessageResponse, UserPasswordModel>(`/recovery/${id}`, model, false)

    return res
}