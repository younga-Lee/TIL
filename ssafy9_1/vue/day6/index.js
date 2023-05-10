// store/index.js

export default new Vuex.Store({
  state: {
    count: 0,
  },
  mutations: {
    NUMBER_INCREMENT: function (state) {
      state.count += 1
    },
  },
  actions: {
    numberIncrement: function (context) {
      context.commit('NUMBER_INCREMENT', count)
    },
  },
})