import React, { Component } from "react";

class Phrase extends Component {
  constructor(props) {
    super(props);
    this.state = {
        wordtotals: [],
        newspapers: [],
        phrase: '',
        loaded: false,
        placeholder: "Loading",
    };
  }

  componentDidMount() {
    console.log('component mounted')

    fetch(`/api/newspaper/`)
      .then((response) => {
        console.log('newspaper response', response)
        return response.json();
      })
      .then((data) => {
        console.log('newspaper data', data);

        let newspapers = {}
        data.results.map((newspaper) => {
          newspapers[newspaper.id] = newspaper.name;
        })

        this.setState({
            newspapers: newspapers
      })
    })

    console.log(this.props.location)
    const { match: { params } } = this.props;
    console.log(params)

    fetch(`/api/phrases/${params.id}`)
      .then((response) => {
        console.log(response);
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        this.setState({
          wordtotals: data.wordtotals,
          phrase: data.phrase,
          loaded: true,
        });
      });
  }

  render() {
    return (
      <div className="container mx-auto">
        <div className="flex flex-col">
          <div className="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
          <h3 class="py-8 mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl sm:leading-10">
        {this.state.phrase}
      </h3>
            <div className="align-middle inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200">
              <table className="min-w-full">
                <thead>
                  <tr>
                    <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                      Date of Appearance
                    </th>
                    <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                      Newspaper
                    </th>
                    <th className="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                      Count
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white">
                  {this.state.wordtotals.map((wordtotal) => {
                    return (
                      <tr key={wordtotal.id}>
                        <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div className="flex items-center">
                            <div className="ml-4">
                              <div className="text-sm leading-5 text-gray-900">
                                  {new Date(wordtotal.wordlist.date).toLocaleDateString('en-GB')}
                              </div>
                            </div>
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div className="text-sm leading-5 text-gray-900">
                            {this.state.newspapers[wordtotal.wordlist.newspaper]}
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div className="text-sm leading-5 text-gray-900">
                            {wordtotal.count}
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Phrase;
