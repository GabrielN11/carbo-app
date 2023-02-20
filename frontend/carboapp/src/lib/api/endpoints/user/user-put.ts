import { apiPut } from "$lib/api/api";
import type { SuccessfullyMessageResponse, SuccessfullyResponse } from "$lib/api/api-models";
import type UserPutModel from "../../../../models/user/user-put-model";

export default async function alterUsername(id: number, model: UserPutModel): Promise<SuccessfullyMessageResponse> {
    const res = await apiPut<SuccessfullyMessageResponse, UserPutModel>(`/user/${id}`, model, true)
    return res
}