<script lang="ts">
	import Icon from "@iconify/svelte";
	import { getContext, afterUpdate } from "svelte";
	import type UserModel from "../models/user/user-model";
	import { page } from "$app/stores";
	import type { Writable } from "svelte/store";
	import { logout, user } from "../stores/user-store";
	import Menu from "@smui/menu";
	import List, { Item, Separator, Text } from "@smui/list";
	import Button, { Label } from "@smui/button";

	let menu: Menu;
</script>

<header>
	<div class="header-container">
		<a href="/">
			<iconify-icon
				icon="fa6-solid:wheat-awn"
				style="color: white;"
				width="25"
			/>
			<h1 class="main-title">Carbo App</h1>
		</a>
	</div>
	<div class="header-container">
		{#if $user}
			<Button color='secondary' on:click={() => menu.setOpen(true)}>
				<Label>
					<div class='user-label'>
						<iconify-icon
						icon="mdi:user"
						style="color: white;"
						width="25"
					/>
					<p>{$user.username}</p>
					</div>
				</Label>
			</Button>
			<Menu bind:this={menu}>
				<List>
				  <Item on:SMUI:action={() => console.log('clicou')}>
					<Text>Perfil</Text>
				  </Item>
				  <Item on:SMUI:action={() => logout()}>
					<Text>Sair</Text>
				  </Item>
				</List>
			  </Menu>
		{:else if $page.route.id !== "/login"}
			<a href="/login">
				<iconify-icon
					icon="ri:login-circle-fill"
					style="color: white"
					width="25"
				/>
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

	.user-label{
		display: flex;
		align-items: center;
		gap: 7px;
	}
	.user-label p {
		margin: 0
	}

	.header-container {
		display: flex;
		gap: 7px;
		align-items: center;
	}

	.header-container a {
		display: flex;
		align-items: center;
		gap: 10px;
		color: #fff;
		cursor: pointer;
	}

	.header-container a p {
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
