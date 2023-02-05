import { apiGet } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";

interface UserId{
    id: number;
}

export default async function validateCode(id: number, code: string): Promise<SuccessfullyResponse<UserId>>{
    const user = await apiGet<SuccessfullyResponse<UserId>>(`/recovery/${id}?code=${code}`, false)
    return user
}