<script lang="ts">
	import getUser from "$lib/api/endpoints/user/user-get";
	import { onMount, setContext } from "svelte";
	import { user } from "../stores/user-store";
	import { loading } from "../stores/loading-store";
	import type UserModel from "../models/user/user-model";
	import Header from "./Header.svelte";
	import "./styles.css";
	import Loading from "../components/loading/loading.svelte";
    import Toast from "../components/toast/toast.svelte";
	async function userWrapper() {
		try {
			if (!localStorage.getItem("usertoken")) return;

			const userData = await getUser();

			user.update((curr) => (curr = userData.data));
		} catch (e: any) {}
	}

	onMount(userWrapper);
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
	<link
		href="https://fonts.googleapis.com/css2?family=Montserrat&family=Roboto&display=swap"
		rel="stylesheet"
	/>
	<link rel="stylesheet" href="/smui.css" />
	<script src="https://code.iconify.design/3/3.0.1/iconify.min.js"></script>
	<script
		src="https://code.iconify.design/iconify-icon/1.0.3/iconify-icon.min.js"
	></script>
</svelte:head>

<div class="app">
	<Header />
	<main>
		<slot />
	</main>
	<Loading />
	<Toast/>
</div>

<style>
	main {
		min-height: calc(100vh - 76px);
	}
</style>
