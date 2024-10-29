<template>
    <header class="bg-green-conaf-700 text-white p-6">
        <div class="container mx-auto">
            <h1 class="text-3xl font-bold text-center mb-4">Calculadora de Huella de Carbono</h1>
            <p class="text-center mb-6">
                Calcula el impacto ambiental de tus servicios de streaming y contribuye a una vida más sostenible.
            </p>
            <nav class="flex justify-center space-x-8">
                <router-link to="/" class="text-lg hover:underline" :class="{ 'font-semibold': $route.path === '/' }">
                    Calculadora
                </router-link>

                <router-link to="/reporte" class="text-lg hover:underline"
                    :class="{ 'font-semibold': $route.path === '/reporte' }">
                    Reporte
                </router-link>
            </nav>
        </div>
    </header>
</template>