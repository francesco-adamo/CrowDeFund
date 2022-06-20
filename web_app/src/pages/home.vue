<template>
  <q-page class="q-pt-md">

    <div class="q-pa-md row full-width flex-grow justify-between">
      <q-card style="width:32%">
        <q-card-section class="bg-indigo text-white">
          <div class="text-h6">My DeFi Game Idea</div>
          <div class="text-subtitle2">by John Doe</div>
        </q-card-section>

        <q-separator />

        <q-card-section class="text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat>Learn more</q-btn>
          <q-btn flat>Contribute now</q-btn>
        </q-card-actions>

        <q-linear-progress stripe rounded size="20px" :value="0.7" color="indigo" class="q-mt-sm" />
      </q-card>

      <q-card style="width:32%">
        <q-card-section class="bg-purple text-white">
          <div class="text-h6">A New Exciting Learning Project</div>
          <div class="text-subtitle2">by MasterZ</div>
        </q-card-section>

        <q-separator />

        <q-card-section class="text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat>Learn more</q-btn>
          <q-btn flat>Contribute now</q-btn>
        </q-card-actions>

        <q-linear-progress stripe rounded size="20px" :value="0.3" color="purple" class="q-mt-sm" />
      </q-card>

      <q-card style="width:32%">
        <q-card-section class="bg-pink text-white">
          <div class="text-h6">GameFi Universe</div>
          <div class="text-subtitle2">by Mario Rossi</div>
        </q-card-section>

        <q-separator />

        <q-card-section class="text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat>Learn more</q-btn>
          <q-btn flat>Contribute now</q-btn>
        </q-card-actions>

        <q-linear-progress stripe rounded size="20px" :value="0.8" color="pink" class="q-mt-sm" />
      </q-card>
    </div>

    <div id="q-app" style="max-height: 100vh" >
    <div class="q-pa-md">
      <q-parallax :height="500" :speed="1">
        <template v-slot:media>
          <video width="1920" height="1080" autoplay loop muted>
            <source type="video/webm" src="~assets/background.webm">
            <source type="video/mp4" src="~assets/background.mp4">
          </video>
        </template>

        <q-icon 
          name="donut_large" 
          class="text-white" 
          style="font-size: 128px;" 
        />
        
        <div class="logo text-h2 text-white text-center">CrowDeFund</div>
        <div class="text-h3 text-white text-center q-mt-xl" style="opacity:0.7">—We believe in your project—</div>
      </q-parallax>
    </div>
  </div>

  <div class="q-pa-md row full-width flex-grow justify-between">
      <q-card style="width:32%">
        <q-card-section class="bg-primary text-white">
          <div class="text-h6">True Decentralized Finance Ecosystem</div>
          <div class="text-subtitle2">by 0xAnonymous</div>
        </q-card-section>

        <q-separator />

        <q-card-section class="text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat>Learn more</q-btn>
          <q-btn flat>Contribute now</q-btn>
        </q-card-actions>

        <q-linear-progress stripe rounded size="20px" :value="0.4" color="primary" class="q-mt-sm" />
      </q-card>

      <q-card style="width:32%">
        <q-card-section class="bg-teal text-white">
          <div class="text-h6">Collectible NFT Trading Card Game</div>
          <div class="text-subtitle2">by NFTMagic64</div>
        </q-card-section>

        <q-separator />

        <q-card-section class="text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat>Learn more</q-btn>
          <q-btn flat>Contribute now</q-btn>
        </q-card-actions>

        <q-linear-progress stripe rounded size="20px" :value="0.9" color="teal" class="q-mt-sm" />
      </q-card>

      <q-card style="width:32%">
        <q-card-section class="bg-green text-white">
          <div class="text-h6">This Invention Will Change The World</div>
          <div class="text-subtitle2">by Algorand Foundation</div>
        </q-card-section>

        <q-separator />

        <q-card-section class="text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat>Learn more</q-btn>
          <q-btn flat>Contribute now</q-btn>
        </q-card-actions>

        <q-linear-progress stripe rounded size="20px" :value="0.6" color="green" class="q-mt-sm" />
      </q-card>
    </div>

    <div class="row full-width flex-grow justify-evenly q-mt-xl q-mb-xl q-pt-xl q-pb-xl">
      <img src="~assets/algorand_logo.png" style="width: 300px">
      <img src="~assets/masterz_logo.jpeg" style="width: 300px">
    </div>

    <div>
      <q-toolbar class="bg-indigo text-white text-right text-caption q-pr-lg">
        <q-toolbar-title class="text-subtitle1">
          Copyright &copy 2022 Team Horizon
        </q-toolbar-title>
      </q-toolbar>
    </div>

  </q-page>
</template>

<script>
  import { defineComponent, ref, computed } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { useStore } from 'vuex';
  import { useQuasar } from 'quasar';

  export default defineComponent({
    name: 'login',
    setup () {
      let username = ref(null);
      let password = ref(null);
      let loading = ref(false);

      const $router = useRouter();
      const $store = useStore();
      const $q = useQuasar();

      const config = {
        address: 'delectron2.francescoadamo.ninja',
        port: '1234'
      };

      async function onSubmit () {
        loading.value = true;
        
        const userData = await getUserData();
        if (!userData) {
          loading.value = false;
          return;
        }

        if (userData.admin) {
          const usersList = await listUsers();
          if (!usersList) {
            loading.value = false;
            return;
          }

          $store.commit('user/setAdministrator', true);
          $store.commit('user/setUsersList', usersList);
        }

        $store.commit('user/setAuthenticated', true);
        $store.commit('user/setUsername', username.value);
        $store.commit('user/setPassword', password.value);
        $store.commit('user/setUserData', userData);

        loading.value = false;

        console.log('DONE!');
        $q.notify({
          type: 'positive',
          message: 'Login successful!',
          timeout: 2000
        });

        if (userData.admin) $router.push('/admin');
        else $router.push('/user');
      }

      // GET USER DATA
      async function getUserData() {
        const options = {
          url: 'https://' + config.address + ':' + config.port + '/userdata',
          method: 'POST',
          headers: {
              'content-type': 'application/json'
          },
          data: {
              user: username.value,
              password: password.value,
          }
        };

        console.log('sending userdata request...');
        let error;
        const response = await axios(options)
        .catch(err => error = err);

        if (error) {
            console.log(error.message);
            if (error.response && error.response.data) console.log(error.response.data);

            $q.notify({
              type: 'negative',
              message: 'Login error: ' + (error.response && error.response.data ? error.response.data.error : error.message),
              timeout: 2000
            });

            return;
        }

        return response.data;
      }

      // GET USERS LIST
      async function listUsers() {
        const options = {
          url: 'https://' + config.address + ':' + config.port + '/listusers',
          method: 'POST',
          headers: {
              'content-type': 'application/json'
          },
          data: {
              user: username.value,
              password: password.value,
          }
        };

        console.log('sending listusers request...');
        let error;
        const response = await axios(options)
        .catch(err => error = err);

        if (error) {
            console.log(error.message);
            if (error.response && error.response.data) console.log(error.response.data);

            $q.notify({
              type: 'negative',
              message: 'Login error: ' + (error.response && error.response.data ? error.response.data.error : error.message),
              timeout: 2000
            });

            return;
        }

        return response.data;
      }

      return {
        username,
        password,
        loading,
        onSubmit
      }
    }
  })
</script>
