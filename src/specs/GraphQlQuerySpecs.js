import assert from "assert"
import GraphQlQuery from "./../util/graphql/GraphQlQuery"

describe("GraphQlQueryBuilder", function(){

  it("should return GraphQlQuery object to query for all games by give type and fields", function(){
    const expected = `
      query{
        allGames(type: "standard"){
          edges{
            node{
              id title
            }
          }
        }
      }`
      const result = GraphQlQuery.getAllGamesByType("standard", ["id", "title"])
      assert.strictEqual(result.query, expected)
  })

})