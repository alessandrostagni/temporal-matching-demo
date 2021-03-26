export function handleRequest(ref: any) {
    const requestOptions = {
      crossDomain: true,
      method: 'POST',
      headers: { 'Content-Type': 'application/json; utf-8' },
      body: JSON.stringify({
        formula: ref.state.formula,
        assignment: ref.state.assignment,
        gamma: ref.state.gamma
      })
    };
    const REACT_APP_API_URL: any = process.env['REACT_APP_API_URL'] + '/get-graph';
    fetch(REACT_APP_API_URL, requestOptions)
        .then(response => response.json()).then(
            data => ref.setState({
                linkStreamData: data.linkStream,
                matchingData: data.matching
            }))
  }