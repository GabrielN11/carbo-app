<script lang="ts">
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import List from "@smui/list";
    import { displayToast } from "../../stores/toast-store";
    import type FoodModel from "../../models/food/food-model";
    import getFood from "$lib/api/endpoints/food/get-food";
    import FoodCard from "../food-card/food-card.svelte";
    import { onMount } from "svelte";

    let query: string = "";
    let page: number = 0;

    let foodList: FoodModel[] = [];

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

    onMount(() => onSubmit());
</script>

<svelte:head>
    <title>Carbo App - Entrar</title>
    <meta
        name="description"
        content="Login no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>
    <form
        on:submit={onSubmit}
    >
        <fieldset>
            <Textfield
                style="width: 100%"
                variant="filled"
                label="Alimento"
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
    <div class="list">
        <List twoLine>
            {#each foodList as food}
                <FoodCard {food} />
            {/each}
        </List>
        <Button touch variant='outlined' color='secondary'>
            <Label>Carregar Mais</Label>
        </Button>
    </div>
</section>

<style>
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

    .list {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }

    @media (min-width: 600px) {
        fieldset {
            width: 400px;
        }
    }
</style>
