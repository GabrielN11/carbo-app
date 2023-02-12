import { apiDelete } from "$lib/api/api";
import type { SuccessfullyMessageResponse } from "$lib/api/api-models";

export default async function deleteFavorite(id: number): Promise<SuccessfullyMessageResponse> {
    const res = await apiDelete<SuccessfullyMessageResponse>(`/favorite/${id}`, true)

    return res
}