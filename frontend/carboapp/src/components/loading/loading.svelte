<script lang="ts">
    import { loading } from "../../stores/loading-store";

    export let size: number = 50;
</script>

{#if $loading}
    <div class="loading-container">
        <div class="spin" style="height: {size}px; width: {size}px" />
    </div>
{/if}

<style>
    .loading-container {
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        z-index: 999;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(0, 0, 0, 0.5);
    }

    .spin {
        border-radius: 50%;
        border: 10px solid var(--mdc-theme-primary, #fff);
        border-right-color: transparent;
        animation: loading 1s infinite;
    }

    @keyframes loading {
        to {
            transform: rotate(360deg);
        }
    }
</style>
