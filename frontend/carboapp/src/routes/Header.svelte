<script lang="ts">
	import Icon from "@iconify/svelte";
	import { getContext } from "svelte";
	import type UserModel from "../models/user/user-model";
	import { page } from "$app/stores";

	const user = getContext<UserModel>("user");
</script>

<header>
	<div class="header-container">
		<a href='/'>
			<Icon icon="fa6-solid:wheat-awn" color="white" height="25" />
			<h1 class="main-title">Carbo App</h1>
		</a>
	</div>
	<div class="header-container">
		{#if user}
			<a href="/">
				<Icon icon="mdi:user" color="white" height="25" />
				<p>{user.username}</p>
			</a>
		{:else if $page.route.id !== "/login"}
			<a href="/login">
				<Icon icon="ri:login-circle-fill" color="white" height="25" />
				<p>Login</p>
			</a>
		{/if}
	</div>
</header>

<style>
	header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 20px;
	}

	.header-container {
		display: flex;
		gap: 7px;
		align-items: center;
	}

	.header-container a{
		display: flex;
		align-items: center;
		gap: 5px;
		color: #fff;
		cursor: pointer;
	}

	.header-container a p{
		margin: 0;
	}

	.main-title {
		margin: 0;
		font-size: 1.5rem;
	}

	@media (max-width: 400px) {
		.main-title {
			font-size: 1rem;
		}
	}
</style>
