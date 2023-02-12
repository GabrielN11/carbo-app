import { apiPost } from "$lib/api/api";
import type { SuccessfullyResponse } from "$lib/api/api-models";
import type FavoriteModel from "../../../../models/favorite/favorite-model";

interface FavoriteId{
    id: number;
}

export default async function postFavorite(model: FavoriteModel): Promise<SuccessfullyResponse<FavoriteId>> {
    const res = await apiPost<SuccessfullyResponse<FavoriteId>, FavoriteModel>('/favorite', model, true)

    return res
}