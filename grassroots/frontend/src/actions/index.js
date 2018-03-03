const FILTER_BY_STATE = "FILTER_BY_STATE"

export function filterCongressBar(state) {
    return {
        type: FILTER_BY_STATE,
        state,
    }
}