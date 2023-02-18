<script lang="ts">
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import List from "@smui/list";
    import { displayToast } from "../../stores/toast-store";
    import type FoodModel from "../../models/food/food-model";
    import getFood from "$lib/api/endpoints/food/get-food";
    import FoodCard from "../food-card/food-card.svelte";
    import { onMount } from "svelte";
    import { listen } from "svelte/internal";
    import getFoodByProfile from "$lib/api/endpoints/food/get-food-by-profile";
    import getFavoriteFood from "$lib/api/endpoints/food/get-favorite-food";

    let query: string = "";
    let page: number = 0;

    let foodList: FoodModel[] = [];

    export let profile: boolean = false;
    export let favorite: boolean = false;
    export let profileId: number | undefined = undefined;

    async function onProfileSubmit(e?: SubmitEvent) {
        if (e) {
            e.preventDefault();
            foodList = [];
            page = 0;
        }
        try {
            const res = await getFoodByProfile(profileId!, query, page);

            foodList = [...foodList, ...res.data];

            if (res.data.length === 10) page += 1;
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 2500);
        }
    }

    async function onFavoriteSubmit(e?: SubmitEvent) {
        if (e) {
            e.preventDefault();
            foodList = [];
            page = 0;
        }
        try {
            const res = await getFavoriteFood(profileId!, page);

            foodList = [...foodList, ...res.data];

            if (res.data.length === 10) page += 1;
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 2500);
        }
    }

    async function onSubmit(e?: SubmitEvent) {
        if (e) {
            e.preventDefault();
            foodList = [];
            page = 0;
        }
        try {
            const res = await getFood(query, page);

            foodList = [...foodList, ...res.data];

            if (res.data.length === 10) page += 1;
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 2500);
        }
    }

    function returnSubmit() {
        if (profile) {
            return onProfileSubmit;
        } else if (favorite) {
            return onFavoriteSubmit;
        } else {
            return onSubmit;
        }
    }

    onMount(() => returnSubmit()());
</script>

<section>
    {#if !favorite}
        <form on:submit={returnSubmit()}>
            <fieldset>
                <Textfield
                    style="width: 100%"
                    variant="filled"
                    label="Pesquisar alimento..."
                    placeholder="Nome ou descrição..."
                    bind:value={query}
                    color="secondary"
                />
            </fieldset>
            <fieldset>
                <Button
                    touch
                    variant="outlined"
                    color="secondary"
                    type="submit"
                    style="width: 100%"
                >
                    <Label>Buscar</Label>
                </Button>
            </fieldset>
        </form>
    {/if}
    <div class="list-container">
        {#if foodList.length === 0}
            <div class="not-found">
                <iconify-icon
                    icon="mdi:food-off"
                    style="color: white;"
                    width="35"
                />
                <h2>Nenhum alimento encontrado.</h2>
            </div>
        {:else}
            <List twoLine class="demo-list">
                {#each foodList as food}
                    <FoodCard {food} />
                {/each}
            </List>
            {#if foodList.length % 10 === 0}
                <Button touch variant="outlined" color="secondary">
                    <Label>Carregar Mais</Label>
                </Button>
            {/if}
        {/if}
    </div>
</section>

<style>
    * :global(.demo-list) {
        width: 600px;
    }
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        padding-top: 20px;
    }

    fieldset {
        width: 254px;
        border: none;
    }

    .list-container {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }

    .not-found {
        display: flex;
        gap: 7px;
        align-items: center;
        justify-content: center;
    }

    @media (min-width: 600px) {
        fieldset {
            width: 400px;
        }
    }

    @media (max-width: 600px) {
        * :global(.demo-list) {
            max-width: 300px;
        }

        .not-found h2 {
            font-size: 1rem;
        }
    }
</style>
