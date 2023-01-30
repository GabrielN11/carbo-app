<script lang='ts'>
    import getUser from "$lib/api/endpoints/user/user-get";
    import { onMount, setContext } from "svelte";
    import type UserModel from "../models/user/user-model";
	import Header from "./Header.svelte";
	import "./styles.css";

	async function userWrapper(){
		try{
			const user = await getUser()

			setContext<UserModel>('user', user.data)
		}catch(e: any){

		}
	}

	onMount(userWrapper)
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
	<link
		href="https://fonts.googleapis.com/css2?family=Montserrat&family=Roboto&display=swap"
		rel="stylesheet"
	/>
	<script src="https://code.iconify.design/3/3.0.1/iconify.min.js"></script>
</svelte:head>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>
</div>

<style>
</style>
