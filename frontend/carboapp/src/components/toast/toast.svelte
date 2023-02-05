<script lang="ts">
    import type ToastModel from "../../models/toast/toast-model";
    import { onMount, afterUpdate } from 'svelte';
    import { toasts } from "../../stores/toast-store";
</script>
    {#if $toasts.length > 0}
    <div class="warning-box">
        {#each $toasts as { color, duration, text }, i}
            <div>
                <div class="warning" style="background-color: {color}">
                    {text}
                </div>
                <div
                    class="warning-bar"
                    style="animation: timer {duration}ms forwards ease-out; background-color: {color}"
                />
            </div>
        {/each}
    </div>
    {/if}

<style>
    .warning-box {
        position: fixed;
        bottom: 50px;
        right: 25px;
        display: flex;
        flex-direction: column-reverse;
        width: fit-content;
        z-index: 15;
    }

    .warning {
        padding: 10px 20px;
        color: #fff;
        margin-top: 10px;
        border-radius: 5px 5px 0px 0px;
        user-select: none;
        background: var(--mdc-theme-error);
    }

    .warning-bar {
        height: 5px;
        background-color: var(--mdc-theme-error);
        opacity: 0.5;
        width: 100%;
        animation: timer 4s forwards ease-out;
    }

    @keyframes -global-timer {
        to {
            width: 0px;
        }
    }
</style>
